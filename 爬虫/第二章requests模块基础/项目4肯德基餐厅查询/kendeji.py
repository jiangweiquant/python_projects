import requests
import json
header = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
         }
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
data = {
    'cname': '',
    'pid': '',
    'keyword': '重庆',
    'pageIndex': '2',
    'pageSize': '5',
}
res = requests.post(url=url, data=data, headers=header)
print(res.status_code)
content = res.text
print(content)

with open('kendeji.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
print('保存成功！')