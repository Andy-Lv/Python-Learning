# url="https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}"  所有章节的内容
# 章节内部内容
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}

import requests
import asyncio
import aiohttp
import json
import aiofiles


async def aioDownload(cid, book_id, title):
    data = {
        "book_id": "4306063500",
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            title = "西游记/" + title + ".txt"
            async with aiofiles.open(title, mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']["content"])


# 同步操作,拿到所有章节的cid和名称
async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        tasks.append(aioDownload(cid, book_id, title))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    book_id = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_id + '"}'
    asyncio.run(getCatalog(url))
