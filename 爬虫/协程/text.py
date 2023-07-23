import json
import requests
def aiodownload():
    import json
    book_id = "224306063500",
    chapter_id = "221569782244"
    data = {"book_id": book_id, "chapter_id": chapter_id}
    data_json = json.dumps(data)  # 将Python字典转换为JSON字符串
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82',
        'Referer':'https://boxnovel.baidu.com/'
    }
    url = f"https://novelapi.baidu.com/boxnovel/cors?uid=&boxnovelTimeStampNow=1690093345329&trace_log=undefined&action=novel&type=content&osname=wise&data={{{data_json}}}"
    res = requests.get(url,headers=header)
    res.encoding ='utf-8'
    print(res.text)


if __name__ == '__main__':
    aiodownload()