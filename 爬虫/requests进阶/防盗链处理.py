import requests
# 1、拿到contId
# 2、拿到video_status返回的json ->srcUrl
# 3、srcUrl里面的内容进行修改
# 4、下载视频
url = 'https://www.pearvideo.com/video_1771601'
contId = url.split('_')[1]

video_status = 'https://www.pearvideo.com/videoStatus.jsp?contId={}&mrd=0.8499'.format(contId)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
    #防盗链【溯源:当前请求的上一级是谁】
    'Referer':  url
}
res = requests.get(video_status,headers=headers)
dic = res.json()

scrUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
scrUrl = scrUrl.replace(systemTime,'cont-'+contId)
# print(scrUrl)
#下载视频
with open('video.mp4','wb') as f:
    f.write(requests.get(url=scrUrl).content)