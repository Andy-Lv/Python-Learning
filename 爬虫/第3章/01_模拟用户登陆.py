# 登陆 -> 得到cookie
# 带着cookie去请求书架url -> url 上的内容
# 必须将上面两个操作连起来
# 我们可以利用session进行请求->session可以认为一连串的请求并且cookie不会丢失

import requests

# 会话
session = requests.session()

data = {
    "loginName": "1234567890",
    "password": "1234567890"
}

# 登陆
url = "https://passport.17k.com/ck/user/login"
resp = session.post(url, data=data)

# 拿书架上的书
resp=session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
