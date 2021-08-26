# 1 找到未加密的参数                    # window.arsea(参数 ,xxx,xxx,xxx,xxx)
# 2 想办法吧参数进行加密, 参考网易的逻辑, params =>rncText, encSecKey => encSecKey
# 3 请求网易, 拿到评论信息
import requests

from Crypto.Cipher import AES

url = "https://interface.music.163.com/weapi/v1/resource/comments/get"

# 请求方式是post
resp = requests.post(url)

data = {
    "crf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_S0_41325905146",
    "threadId": "R_S0_41325905146"
}

#处理加密过程
