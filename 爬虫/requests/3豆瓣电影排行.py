import requests
import json
#1指定url
url = 'https://movie.douban.com/j/chart/top_list'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
dic = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}
# 2发送请求获得响应对象
response = requests.get(url=url, headers=headers, params=dic)
# 3获取响应对象的内容，text返回的是字符串内容
content = response.json()
response.close()
# 4存储内容
fp = open('moive_rank.json','w',encoding='utf-8')
json.dump(content,fp=fp,ensure_ascii=False)
print('over')
