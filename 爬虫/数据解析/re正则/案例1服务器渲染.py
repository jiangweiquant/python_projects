import requests
import re
import csv
#1、爬取数据
url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
response = requests.get(url=url, headers=headers)
content = response.text
# print(content)

#2、解析数据[需求：名字，年份，评分，多少人评估]
obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<grades>.*?)</span>.*?<span>(?P<nums>.*?)</span>', re.S)
result = obj.finditer(content)
f = open('data.csv',mode='w',encoding='utf-8')
csvwriter = csv.writer(f)
for i in result:
    # print(i.group('name'))
    # print(i.group('year').strip())
    # print(i.group('grades'))
    # print(i.group('nums'))
    dict = i.groupdict()
    dict['year'] = dict['year'].strip()
    print(dict.values())
    csvwriter.writerow(dict.values())
f.close()
print('over')