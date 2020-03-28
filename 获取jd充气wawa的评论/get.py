import requests
import json
import time
import jieba
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image

PRODUCTID = "1263013576"
BASE_URL = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=" \
           "%s&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1"

had = 1 # 还有更多
page = 1 # 页码数

# 构造请求头
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer' : 'https://item.jd.com/%s.html' % PRODUCTID
}


# 获取评论信息
def get_comment(url):
    try:
        # 执行请求，获取结果
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        print('字符编码', res.encoding)

    except Exception as e:
        print('get comment errors')
        raise e

    # 去掉多余字符，并从字节转为字符串
    json_str = res.content[20:-2].decode(res.encoding)

    # json转为对象
    con = json.loads(json_str)
    # print(con)
    # raise Exception('exit')

    return con['comments']

def do_spider(page):
    # 抓取100页
    for i in range(100):
        print('正在获取第%d页...' % i)
        res = get_comment(BASE_URL % (PRODUCTID, page))
        if res != []:
            for r in res:
                with open('comments.txt', 'a+', encoding="utf-8") as f:
                    f.write(r["content"]+"\n", )
        page += 1
        time.sleep(5)
        # print(res)


# 分词
def cut_word():
    """
    对数据进行分词
    :return: 分词后的数据
    """
    with open('comments.txt', encoding="utf-8") as f:
        comment_text = f.read()
        wordlist = jieba.cut(comment_text, cut_all=True)
        wl = " ".join(wordlist)
        print(wl)
        return wl

def create_word_cloud():
    """
    生成词云
    :return:
    """
    # 设置词云形状图片
    coloring = np.array(Image.open("wawa.jpg"))
    # 设置词云的一些配置， 如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color="white", max_words=2000, mask=coloring, scale=4,
                   max_font_size=50, random_state=42, font_path="C:\Windows\Fonts\simsun.ttc")
    # 生成词云
    wc.generate(cut_word())

    # 在只设置mask的情况下，你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure(num=1, figsize=(12,8))
    plt.savefig('word_cloud.jpg')
    plt.show()





if __name__ == "__main__":
    create_word_cloud()
    pass