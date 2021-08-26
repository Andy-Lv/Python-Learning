import asyncio
import aiohttp
import aiofiles

urls = {
    "http://kr.shanghai-jiuxin.com/file/2020/1029/bf3b122b6e1ddd9777dadc6ca97b22e6.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/0316/1383df6982db26460d655d67c3dc4726.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0429/3f381541926e01ece21fd210f59af6d2.jpg"
}


async def aiodownload(url):
    name = url.rsplit("/", 1)[1]
    # aiohttp.ClientSession() <=> requests
    async with aiohttp.ClientSession() as session:  # requests
        async with session.get(url) as resp:  # resp=requests.get()
            async with aiofiles.open(name, mode="wb") as f:  # 写入文件
                await f.write(await resp.content.read())  # 读取内容是异步的,需要await


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
