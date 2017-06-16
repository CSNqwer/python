
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.manager = url_manager.Manager()
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.outputer = html_outputer.Outputer()

    def craw(self, root_url):
        ss = 1
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url():
            try:
                new_url = self.manager.get_new_url()
                print 'No. %d  WEB: %s' % (ss,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.manager.add_new_urls(new_urls)
                self.outputer.collect_datas(new_data)
                ss = ss + 1
                if ss == 1000:
                    break
            except:
                print "crow failed"
        self.outputer.output_html()
        print '111'

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
