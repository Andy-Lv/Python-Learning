import requests

url = "https://movie.douban.com/j/search_tags"
# 如果url参数过长，可以选择重新封装参数
param = {
    "type": "movie",
    "source": "index",
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

resp = requests.get(url, params=param, headers=headers)  # 注意参数不唯一时需要加s

print(resp.request.url)
print(resp.text)
resp.close()
