# 想要抓取一个视频:
# 1 找到m3u8
# 2 通过m3u8下载ts文件
# 3 通过各种手段将ts合并成mp4文件


import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36"
}

url = "https://www.91kanju.com/vod-play/59946-1-1.html"
resp = requests.get(url, headers=headers)

obj = re.compile(r"url: '(?P<m3u_url>.*?)',", re.S)  # 提取m3u8的地址
m3u8_url = obj.search(resp.text).group("m3u_url")  # 拿到m3u8的地址

resp.close()

# 下载m3u8文件
resp2 = requests.get(m3u8_url, headers=headers)

with open("你是我的荣耀.m3u8", mode="wb") as f:
    f.write(resp2.content)

resp2.close()

# 解析m3u8文件
with open("你是我的荣耀.m3u8", mode="r") as f:
    n = 1  # 记录下载片段个数
    for line in f:
        line = line.strip()  # 去掉空格,空白,换行符
        if line.startswith("#"):  # 如果是以"#"开头的我不要
            continue

        # 下载片段
        resp3 = requests.get(line)
        a = open(f"你是我的荣耀/{n}.ts", mode="wb")
        a.write(resp3.content)
        n += 1
        a.close()
        resp3.close()

    f.close()

# 合并视频