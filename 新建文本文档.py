import urlparse


import urllib2
import re

from bs4 import BeautifulSoup
url = "http://baike.baidu.com/item/%E6%BD%98%E6%85%A7%E5%A6%82"
html_cont = urllib2.urlopen(url).read()
soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')


def _get_new_urls(url, soup):
    new_urls = set()
    links = soup.find_all('a', href=re.compile(r"/item/"))
    new_urls = set()
    links = soup.find_all('a', href=re.compile(r"/item/%"))
    print links
    for link in links:
        print link
        new_url = link['href']
        print  new_url
        new_full_url = urlparse.urljoin(url, new_url)
        print new_full_url
        new_urls.add(new_full_url)
_get_new_urls(url,soup)

