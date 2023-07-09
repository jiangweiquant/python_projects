import requests
import json
header = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
post_url = 'https://fanyi.baidu.com/sug'
# post请求参数处理
word = input('enter a word:')
data = {
    'kw':word
}
response = requests.post(url=post_url,data=data, headers=header)
print(response.status_code)
content = response.json()
# 持久化处理
filename = word+'.json'
fp = open(filename,'w',encoding='utf-8')
json.dump(content,fp=fp,ensure_ascii=False)
print(filename,'保存成功！')