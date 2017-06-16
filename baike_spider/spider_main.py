import html_downloader
import html_outputer
import html_parser
import url_manager


class Spidermain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.Html_Outputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count = count + 1
                if count == 1000:
                    break


        self.outputer.output_html()
csnmon

if __name__=="__main__":
    root_url = "http://baike.baidu.com/item/%E6%BD%98%E6%85%A7%E5%A6%82"
    obj_spider = Spidermain()
    obj_spider.craw(root_url)
    1