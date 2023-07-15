import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
response = requests.get(url=url,headers=headers)
content = response.text
# print(content)

#解析数据
page = BeautifulSoup(content, 'html.parser')
# sapn = page.find_all('span', class_="title")#class是python中的关键字，为了区分calss_
sapn = page.find_all('span', attrs={'class':'title'})
print(sapn[0].text)
