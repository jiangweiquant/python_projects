#1、定位到2023年必看热片
#2、从2023年必看热片提取子页面的链接地址
#3、请求子链接的链接地址，拿到想要的下载地址

import requests
import re
#1、爬取数据
url = 'https://www.dy2018.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
response = requests.get(url=url, headers=headers)
response.encoding = 'gb2312'
content = response.text

#2、解析数据
obj1 = re.compile(r'2023必看热片.*?<ul>(?P<url>.*?)</ul>', re.S)
obj2 = re.compile(r"href='(?P<href>.*?)'", re.S)
result1 = obj1.finditer(content)
url_child_list= []
for i in result1:
    url_li = i.group('url').strip()
    # print(url_li)
    #提取子页面链接
    result2 = obj2.finditer(url_li)
    for it in result2:
        # print(it.group('href'))
        url_child = url + it.group('href')#拼接
        # print(url_child)
        url_child_list.append(url_child)

#拿到了所有子链接，提取子页面内容
obj3 = re.compile(r'片　　名　(?P<moive_name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<load_address>.*?)">magnet', re.S)

for href in url_child_list:
    res = requests.get(href, headers=headers)
    res.encoding = 'gb2312'
    result3 = obj3.search(res.text)
    print(result3.group('moive_name'))
    print(result3.group('load_address'))
    # break



