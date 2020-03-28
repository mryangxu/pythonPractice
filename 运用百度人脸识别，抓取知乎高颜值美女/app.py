import time
import os
import re
import requests
from lxml import etree
from aip import AipFace
import base64
import logging

# 配置日志记录信息
logging.basicConfig(filename='log.txt', level=logging.INFO)

# 百度云 人脸识别 申请信息
# 唯一必须填的地址就这三行
APP_ID = "19035409"
API_KEY = "D1AZ6NM3qGYnCqVm83gvUuK5"
SECRET_KEY = "8G0Wic9hujC2EYwzGTXXms2c9o3cde5q"

# 文件存放目录名，相对于当前目录
DIR = "image"
# 过滤颜值阙值，存储空间大的请随意
BEAUTY_THRESHOLD = 10
# 如果权限错误，在浏览器中打开知乎，在开发者中复制一个，不用登陆
# 建议最好换一个，因为不知道知乎的反爬虫策略，如果太多人用同一个，可能会影响程序运行
# 如何替换该值，下文有描述
AUTHORIZATION = "oauth k3N4O8UMvhpqyv3oSc24WaPMLnxhis3O"
# 以下无需改动
# 每次请求知乎的讨论列表，不建议太长，注意节操
LIMIT = 5
# 这是话题【美女】的id
SOURCE = "19552207"
# 爬虫假装下正常浏览器
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
REFERER = "https://www.zhihu.com/topic/%s/newest" % SOURCE
# 某话题下讨论列表的请求url
BASE_URL = "https://www.zhihu.com/api/v4/topics/%s/feeds/timeline_activity" % SOURCE
# 初始请求url， 附带的请求参数
URL_QUERY = "?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=5&offset=1585118946.0"

# 指定 url， 获取对应原始内容/图片
def fetch_image(url):
    try:
        headers = {
            "User-Agent" : USER_AGENT,
            "Referer" : REFERER,
            # "authorization" : AUTHORIZATION
        }
        s = requests.get(url, headers=headers)
    except Exception as e:
        print('fetch last activities fail.' + url)
        raise e

    return s.content

# 指定url， 获取对应json返回/话题列表
def fetch_activities(url):
    try:
        headers = {
            "User-Agent": USER_AGENT,
            "Referer": REFERER,
            # "authorization": AUTHORIZATION
        }
        s = requests.get(url, headers=headers)
    except Exception as e:
        print('fetch last activities fail.' + url)
        raise e
    return s.json()

# 处理返回的话题列表
def process_activities(datums, face_detective):
    if datums['data'] == []:
        print('没有获取到数据，直接获取下一个')
        return datums['paging']['next']
    for data in datums["data"]:
        target = data["target"]
        if "content" not in target or "question" not in target or "author" not in target:
            continue
        # 解析列表中每一个元素的内容
        html = etree.HTML(target["content"])


        seq = 0
        #question_url = target["question"]["url"]
        question_title = target["question"]["title"]
        author_name = target["author"]["name"]
        #author_id = target["author"]["url_token"]
        print('current answer: ' + question_title + " author: " + author_name)
        # 获取所有图片地址
        images = html.xpath("//img/@src")

        print(datums['paging'])
        # raise Exception('阻止向下执行')
        if images == []:
            print('没有图片')
            # 获取后续讨论列表中的请求
            return datums['paging']['next']
        for image in images:
            if not image.startswith("http"):
                continue

            s = fetch_image(image)
            # 请求人脸检测服务
            scores = face_detective(s)
            for score in scores:
                filename = ("%d--" % score) + author_name + "--" + question_title + ("--%d" % seq) + ".jpg"
                filename = re.sub(r'(?u)[^-\w.]', '_', filename)
                # 注意文件名的处理，不同平台非法字符不一样，这里只做了简单的处理，特别是antor_name /question_title 中的内容
                seq = seq + 1
                with open(os.path.join(DIR, filename), 'wb') as fd:
                    fd.write(s)
                    # 人脸检测免费 但有QPS限制
                    time.sleep(2)
                    print(datums['paging'])
                    print('还有吗', datums['paging']['is_end'])
                    # if not datums['paging']['is_end']:
                    # 获取后续讨论列表中的请求
                    return datums['paging']['next']
                    # else:
                    #     return None

def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '_', s)

def init_face_detective(app_id, api_key, secret_key):
    client = AipFace(app_id, api_key, secret_key)
    # 人脸检测中，在响应中附带额外的字段，年龄/性别/颜值/质量
    options = {"face_field": "age,gender,beauty,qualities"}

    def detective(image):
        # print(image.decode('utf-8'))
        # raise Exception('exit')
        # print(base64.b64encode(image).decode('utf-8'))
        r = client.detect(base64.b64encode(image).decode('utf-8'), "BASE64", options)
        # print(r)
        scores = []
        if r['error_code'] == 0:
            # 如果没有检测到人脸
            if r['result']["face_num"] == 0:
                print('没有检测到脸')
                return []
            for face in r['result']['face_list']:
                print(face)
                # 人脸置信度太低
                if face['face_probability'] < 0.6:
                    print('人脸置信度太低')
                    continue
                # 真实人脸置信度太低
                # if face['gender']['type'] !='human':
                #     print('真实人脸置信度太低')
                #     continue
                # 颜值低于阙值
                if face["beauty"] < BEAUTY_THRESHOLD:
                    print('颜值低于阙值')
                    continue
                # 排除非女性
                if face['gender']['type'] != "female":
                    print('排除非女性')
                    continue
                scores.append(face['beauty'])
        return scores
    return detective

def init_env():
    if not os.path.exists(DIR):
        os.makedirs(DIR)


init_env()
face_detective = init_face_detective(APP_ID, API_KEY, SECRET_KEY)
url = BASE_URL + URL_QUERY
while url is not None:
    print('current url:' + url)
    datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    logging.info(datetime + 'current url:' + url)
    datums = fetch_activities(url)
    # print(datums)
    # raise Exception('结束')
    # print(datums["data"])
    url = process_activities(datums, face_detective)
    print('返回的url', url)
    # 注意节操，爬虫休息间隔不要调小
    time.sleep(5)

