from urllib import request
import json
def fetch_data(url):
    with request.urlopen(url) as f:
        res = f.read().decode('utf-8')
        return json.loads(res)
        # print(res)


# 测试
URL = 'https://yesno.wtf/api'
data = fetch_data(URL)
print(data)
assert data['answer'] == 'no'
# assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')