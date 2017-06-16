import urlparse
import re
from bs4 import BeautifulSoup

class Parser(object):
    def parse(self,new_url, html_download):
        if new_url is None or html_download is None:
            return
        soup = BeautifulSoup(html_download,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(new_url,soup)
        new_datas = self._get_new_datas(new_url,soup)
        return new_urls,new_datas

    def _get_new_urls(self, new_url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"/item/"))
        for link in links:
            new_url_short = link['href']
            new_urls_full = urlparse.urljoin(new_url,new_url_short)
            new_urls.add(new_urls_full)
        return new_urls

    def _get_new_datas(self, new_url, soup):
        new_datas = {}
        new_datas['url'] = new_url
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        if title_node != None:
            new_datas['title'] = title_node.get_text()
        else:
            new_datas['title'] = None

        summary_node = soup.find('div',class_='lemma-summary')
        if summary_node != None:
            new_datas['summary'] = summary_node.get_text()
        else:
            new_datas['summary']  = "none"
        return new_datas