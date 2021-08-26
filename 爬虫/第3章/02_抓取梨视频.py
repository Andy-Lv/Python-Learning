# 拿到contId
# 拿到cideoStatus返回的json->srcURL
# srcURL里面的内容进行修正
# 下载视频

import requests

url = "https://www.pearvideo.com/video_1737853"
contId = url.split("_")[1]

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
    # 防盗链:溯源,当前本次请求的上一级是谁
    "Referer": url
}

videoStatus = "https://www.pearvideo.com/videoStatus.jsp?contId=1737853&mrd=0.9536392084296583"

resp = requests.get(videoStatus, headers=headers)

systemTime = resp.json()['systemTime']

srcURL = resp.json()['videoInfo']['videos']['srcUrl']

srcURL = srcURL.replace(systemTime, f"cont-{contId}")

print(srcURL)

with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcURL).content)
