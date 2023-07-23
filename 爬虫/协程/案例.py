import requests
import asyncio
import json
import aiohttp
import aiofiles

async def aiodownload(book_id,chapter_id,chapter_title):
    data = {"book_id": book_id, "chapter_id": chapter_id}
    data_json = json.dumps(data)  # 将Python字典转换为JSON字符串
    url = f"https://novelapi.baidu.com/boxnovel/cors?uid=&boxnovelTimeStampNow=1690093345329&trace_log=undefined&action=novel&type=content&osname=wise&data={{{data_json}}}"
    # print(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content_url=await resp.json()#['data']['url']
            await content_download(content_url,chapter_title)


async def content_download(url,chapter_title):
    res = requests.get(url)
    res.encoding = 'utf-8'
    async with aiofiles.open(chapter_title,'w',encoding='utf-8') as f:
        await f.write(res.text)


async def chapter_download(chapter_url,book_id):
    res = requests.get(chapter_url)
    chapterInfo = res.json()['data']['chapter']['chapterInfo']
    # print(chapterInfo)
    tasks = []
    for chapter in chapterInfo:
        chapter_title = chapter['chapter_title']
        chapter_id = chapter['chapter_id']
        # print(chapter_id,chapter_title)
        tasks.append(asyncio.create_task(aiodownload(book_id,chapter_id,chapter_title)))
    await asyncio.wait(tasks)
if __name__ == '__main__':
    book_id = '4306063500'
    chapter_url = f'https://boxnovel.baidu.com/boxnovel/wiseapi/chapterList?bookid={book_id}&pageNum=1&order=asc&site='
    asyncio.run(chapter_download(chapter_url, book_id))



    # content_url = 'https://boxnovel.baidu.com/boxnovel/content?gid=4306063500&data=%7B%22fromaction%22%3A%22dushu%22,%22fromaction_original%22%3A%22dushu%22%7D&cid=1569782244'
# book_id 4306063500
#
# chapter_id 1569782244
# chapter_title 第一回 灵根育孕源流出 心性修持大道生

























