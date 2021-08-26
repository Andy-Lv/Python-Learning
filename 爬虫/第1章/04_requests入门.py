import requests

url = "https://fanyi.baidu.com/sug"

words = input("请输入你要翻译的英文：")
dat = {"kw": words}

# 发送post请求,发送的数据必须放在字典中，通过data参数进行传递
resp = requests.post(url, data=dat)

print(resp.json())
resp.close()
