#爬取搜狗首页的页面数据
import requests
#1指定url
url = 'https://www.sogou.com/'
# 2发送请求获得响应对象
response = requests.get(url=url)
# 3获取响应对象的内容，text返回的是字符串内容
content = response.text
# 4存储内容
with open('sougou.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
