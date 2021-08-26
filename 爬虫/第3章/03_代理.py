import requests

proxies = {
    "https": "###"  # 你所代理的IP
}

resp = requests.get("https:www.baidu.com", proxies=proxies)
resp.encoding = 'utf-8'
