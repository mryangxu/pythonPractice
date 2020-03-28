import requests
import time
import json
import os
import base64

def get_token_for_baidu():
    """
    从百度获取token, 并写入文件
    :return: token
    """
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=D1AZ6NM3qGYnCqVm83gvUuK5&client_secret=8G0Wic9hujC2EYwzGTXXms2c9o3cde5q'
    response = requests.get(host)
    if response:
        json_str = response.json()
        data = {'access_token': json_str['access_token'], 'expores': time.time() + json_str['expires_in']}
        # return json.dumps(data)
        with open('access_token.json', 'w') as f:
            f.write(json.dumps(data))
        return json_str['access_token']

# 获取token
def get_access_token():

    # 检测文件是否存在 不存在则创建
    if not os.path.exists('access_token.json'):
        os.mknod('access_token.json')

    # 读取文件
    with open('access_token.json', 'r') as f:
        res = f.read()

    # 如果为空文件
    if res == '':
        return get_token_for_baidu()
    # 不为空
    else:
        # json 转为对象
        obj = json.loads(res)

        # 过期了
        if time.time() > obj['expores']:
            return get_token_for_baidu()

        # 没过期
        return json.loads(res)['access_token']


# 执行检测
def exec_detect(image):

    try:

        # 接口地址
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

        # 获取token
        access_token = get_access_token()

        # 拼接地址
        request_url = request_url + '?access_token=' + access_token


        params = {
            'image': image,
            'image_type': 'BASE64',
            'face_field': 'age,beauty,gender',
            'max_face_num': 2
        }

        # print(params)
        # raise Exception('exit')
        headers = {
            'content-type': 'application/json'
        }

        res = requests.post(request_url, data=params, headers=headers)
        return res.content
    except Exception as e:
        print('get errors')
        raise e

# 检测是否是图片文件
def check_img(img):
    imgType_list = {'.jpg', '.bmp', '.png', '.jpeg', '.rgb', '.tif'}
    if os.path.splitext(img)[1] in imgType_list:
        return True
    return False






if __name__ == '__main__':

    # 当前文件下的所有文件
    for filename in os.listdir():

        # 判断是否是图片
        if check_img(filename):

            #打开文件
            with open(filename, 'rb') as f:
                res = f.read()

            # 转为base64
            base64_img = base64.b64encode(res).decode('utf-8')

            # 执行检测
            res = exec_detect(base64_img)

            # 转为json
            res = json.loads(res.decode('utf-8'))

            # 解析成功
            if res["error_code"] == 0:
                if res["result"]["face_num"] < 1:
                    print('没有分析到脸')
                else:
                    for i in res["result"]['face_list']:
                        print('%s 的信息-----评分：%s, 性别：%s，年龄：%s' % (filename, i["beauty"], '女' if i["gender"]["type"] == 'female' else '男', i["age"]))
            else:
                print('解析失败了')

            # 因为百度接口 qbs限制 休息两秒
            time.sleep(2)
