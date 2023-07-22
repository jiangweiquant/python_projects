import requests

proxies = {
    'https':'https://113.78.190.20:1111'
}
res = requests.get('https://www.baidu.com', proxies=proxies)
res.encoding = 'utf-8'
print(res.text)




# 免费代理ip  125.65.40.199:12345