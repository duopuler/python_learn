#encoding:utf-8
from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup
req = request.Request("https://www.baidu.com")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER")
resp = request.urlopen(req)

print(resp.read().decode("utf-8"))
