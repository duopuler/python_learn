# encoding:utf-8
# 网页解析器>>>>>beautiful soup4
import re
from bs4 import BeautifulSoup
from urllib import parse


class HtmlParser(object):
    
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        old_data = self._get_new_datas(page_url, soup)
        return new_urls, old_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.htm     根据实际URL结构进行调整  获取新的URL   https://baike.baidu.com/item/Python
        links = soup.find_all('a', href=re.compile(r'/item/python/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_datas(self, page_url, soup):
        # 解析数据 >>>>>>根据需求调整
        res_data = {}
        # URL
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')      # class为python关键字,因此使用要加_
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data





