import asyncio
import aiohttp

urls = [
    'https://www.toopic.cn/public/uploads/small/1658045021629165804502117.jpg',
    'https://www.toopic.cn/public/uploads/small/165804485495165804485483.jpg',
    'https://www.toopic.cn/public/uploads/image/20200404/20200404182849_78999.jpg'
]

async def aiodownload(url):
    name = url.split('/')[-1]
    # #发送请求
    # s = aiohttp.ClientSession() -> requests
    # s.get() s.post -> requests.get()  requests.post()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # resp.content.read() #->resp.content
            # resp.text() #-> resp.text
            # resp.json()  #-> resp.json()
            #这里也是一个io操作，可以学习aiofiles模块
            with open('imag/'+name,'wb') as f:
                f.write(await resp.content.read())
    print(name,'搞定')

async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())