# encoding:utf-8

from urllib import request
from bs4 import BeautifulSoup
from myLog import Mylog as mylog

class Item(object):
    title = None        # 帖子标题
    firstAuther = None  # 发帖人
    firstTime = None    # 帖子创建时间
    reNum = None        # 总回复数
    content = None      # 最后回复内容
    lastAuther = None   # 最后回复者
    lastTime = None     # 最后回复时间
    
    
class GetTiebaInfo(object):
    def __init__(self,url):
        self.url = url
        self.log = mylog()
        self.pageSum = 5
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

    def getUrls(self, pageSum):
        urls = []
        pns = [str(i*50) for i in range(pageSum)]
        ul = self.url.split('=')
        for pn in pns:
            ul[-1] = pn
            url = '='.join(ul)
            urls.append(url)
        self.log.info('获取Urls成功')
        return urls

    def spider(self, urls):
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'html.parser')
            tagli = soup.find_all('li',attrs={'class':'j_thread_listclearfix'})

            for tag in tagli:
                item = Item()
                item.title = tag.find('a',attrs={'class':'j_th_tit'}).get_text().strip()
                item.firstAuther = tag.find('span',attrs={'class':'frstauthor-name-wrap'}).a.get_text().strip()
                item.firstTime = tag.find('span', attrs={'title': '创建时间'.encode('utf-8')}).get_text().strip()
                item.reNum = tag.find('span', attrs={'title': '回复'.encode('utf-8')}).get_text().strip()
                item.content = tag.find('div', attrs={'class': 'threadlist_abs threadlist_abs_onlyline'}).get_text().strip()
                item.lastAuthor = tag.find('span', attrs={'class': 'tb_icon_author_rely j_replyer'}).a.get_text().strip()
                item.lastTime = tag.find('span', attrs={'title': '最后回复时间'.encode('utf-8')}).get_text().strip()
                items.append(item)
                self.log.info('获取标题为<<%s>>的项成功 ...' %item.title)
            return items

    def pipelines(self, items):
        fileName = '百度贴吧_权力的游戏.txt'.encode('GBK')
        with open(fileName,'w') as fp:
            for item in items:
                fp.write('title:%s \t author:%s \t firstTime:%s \n content:%s \n return:%s \n lastAuthor:%s \t lastTime:%s \n\n\n\n'
                         %(item.title.encode('utf-8'),item.firstAuthor.encode('utf-8'),item.firstTime.encode('utf-8'),item.content.encode('utf-8'),
                           item.reNum.encode('utf-8'),item.lastAuthor.encode('utf-8'),item.lastTime.encode('utf-8')))
                self.log.info('标题为<<%s>>的项输入到"%s"成功' %(item.title,fileName.decode('GBK')))

    def getResponseContent(self,url):
        '''使用一个函数返回页面返回值,便于加入headers与代理服务器'''

        try:
            response = request.urlopen(url.encode('utf-8'))
        except:
            self.log.error('python 返回URL:%s 数据失败' %url)
        else:
            self.log.info('python返回URL:%s 数据成功' %url)
            return response.read()

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=50'
    GTI = GetTiebaInfo(url)