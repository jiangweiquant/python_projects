# 爬取搜狗指定词条对应的搜索结果页面
import requests
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = 'https://www.google.com/search'
kw = input('请输入搜索的词条:')
# 处理url携带的参数：封装到字典里
param = {
    'q': kw
}
response = requests.get(url=url, params=param, headers=header)
content = response.text
filename = kw+'.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(content)
print(filename,'保存成功！')

