# 需求：爬取58二手房中的房源信息
import requests
from lxml import etree

#第一步从网站中爬取页面源码数据
url = 'https://cq.58.com/yubei/ershoufang/'
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
page_text = requests.get(url=url, headers=header).text
with open('ershoufang.thml','w', encoding='utf-8') as fp:
    fp.write(page_text)
#数据解析
tree = etree.HTML(page_text)
div_list = tree.xpath('//section[@class="list"]/div')
print(div_list)
fp = open('58.txt','w',encoding='utf-8')
for div in div_list:
    title = div.xpath('.//h3[@class="property-content-title-name"]/text()')[0]
    print(title)
    fp.write(title+'\n')
