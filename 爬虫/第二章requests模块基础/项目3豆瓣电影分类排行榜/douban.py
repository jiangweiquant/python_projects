import requests
import json
header = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Cookie':'ll="108309"; bid=o29dwWQuju8; _pk_id.100001.4cf6=82c754a5d717d817.1686975058.; __yadk_uid=jsTXj5AFTQ1XwhnT6hfmBn3unGXsJXhv; _vwo_uuid_v2=D9C29030C80CA479D07D2A711365873A0|2f1851a141e94eeaeada502688abb9a2; _ga=GA1.1.1947421099.1686984089; _ga_Y4GN1R87RG=GS1.1.1686984089.1.0.1686984092.0.0.0; ap_v=0,6.0; __utma=30149280.1355890372.1686975034.1686975034.1686984102.2; __utmc=30149280; __utmz=30149280.1686984102.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.477069482.1686975058.1686975058.1686984102.2; __utmb=223695111.0.10.1686984102; __utmc=223695111; __utmz=223695111.1686984102.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1686984114%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utmt_douban=1; __utmb=30149280.5.10.1686984102',
    'Referer': 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=',
    'Host': 'movie.douban.com',
    'Connection': 'keep-alive',
         }
url = 'https://movie.douban.com/j/chart/top_list'
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20',
}
res = requests.get(url=url, params=param, headers=header)
print(res.status_code)
# content = response.json()

# fp = open('douban.json','w',encoding='utf-8')
# json.dump(content,fp=fp,ensure_ascii=False)
# print('保存成功！')