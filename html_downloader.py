#encoding:utf-8
# html 下载器 urllib方法 requests 方法
from urllib import request

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return
        else:
            response = request.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()
