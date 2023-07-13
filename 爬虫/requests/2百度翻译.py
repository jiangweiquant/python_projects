import requests
#1指定url
url = 'https://fanyi.baidu.com/sug'
s = input('请输入单词:')
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
dic = {'kw': s}
# 2发送请求获得响应对象
response = requests.post(url=url, data=dic)
# 3获取响应对象的内容，text返回的是字符串内容
content = response.json()
print(content)
# # 4存储内容
# with open('mysogou.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)
# print('over')
