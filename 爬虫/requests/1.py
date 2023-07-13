import requests
#1指定url
query = input('请搜索一个明星:')
url = f'http://sogou.com/web?query={query}'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
# 2发送请求获得响应对象
response = requests.get(url=url,headers=headers)
print(response)
# 3获取响应对象的内容，text返回的是字符串内容
content = response.text
print(content)
# 4存储内容
file_name = query
with open(file_name+'.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
print('over')
