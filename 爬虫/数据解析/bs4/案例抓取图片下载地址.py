import requests
from bs4 import BeautifulSoup
url = 'https://www.umei.cc/gaoxiaotupian/baoxiaotupian/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
response = requests.get(url=url,headers=headers)
content = response.text
# print(content)
#解析数据
href_list = []
page = BeautifulSoup(content, 'html.parser')
divs = page.find_all('div', class_="img")#<div class="img">
for div in divs:
    a = div.find('a')
    href = a.get('href')
    href = url + href.split('/')[-1]
    # print(href)
    # break
    href_list.append(href)

for href in href_list:
    res = requests.get(url=href, headers=headers)
    res.encoding = 'utf-8'
    link = BeautifulSoup(res.text, 'html.parser')
    img = link.find('div', class_="big-pic").find('img') #<div class="big-pic"><a href=""><img alt="" src="https://www.umei.cc/d/file/20230516/5a16e18b6cb5a14d2b7399952f0d9150.jpg" /></a></div>
    src = img.get('src')
    #下载图片
    img_resp = requests.get(src)
    img_name = src.split('/')[-1]
    with open('imgs/'+img_name,'w',encoding='utf-8') as file:
        file.write(img_resp.text)#图片内容写入文档
    print('over',img_name)
print('all over')