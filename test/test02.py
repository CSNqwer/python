# coding=utf-8
import re
import unittest

from selenium import webdriver
import time

import login


class Test(unittest.TestCase):
    def setUp(self):
        # 用chrome的Mobile emulation模拟手机浏览器测试手机网页
        WIDTH = 320
        HEIGHT = 640
        PIXEL_RATIO = 3.0
        UA = 'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM-G9280 Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.5) WindVane/8.0.0 1440X2560 GCanvas/1.4.2.21'
        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                           "userAgent": UA}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.set_window_size(330,740)
        self.driver.get("http://m.8673h.com")
    def tearDown(self):
        pass
    # 登录
    # def login(self, username, password):
    #     self.driver.find_element_by_xpath("//*[@id='container']/div[2]/div[1]/div/div[2]/span").click()
    #     self.driver.find_element_by_id("loginname1").send_keys(username)
    #     self.driver.find_element_by_id('code1').send_keys(password)
    #     self.driver.find_element_by_id('tcode1').click()
    def  test_xipabaoyang(self):
        self.driver.implicitly_wait(10)
        #登录
        login.Login().login(self.driver, '15140578771', '111111')
        time.sleep(5)
        #判断是否登录成功
        def is_login_succes(driver):
            cookies = driver.get_cookies()
            print  len(cookies)
            len(cookies) == 4

        is_login_succes(self.driver)
        time.sleep(2)
        # 进入小保养
        self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/a').click()
        time.sleep(5)
        default_car = self.driver.find_element_by_xpath('//*[@id="container"]/section/div[1]/div').text
        print (u'默认车型是：%s'%default_car)
        # 更换车型为：宝骏/乐驰/2010款 1.0L P-TEC手动优越型
        self.driver.find_element_by_xpath('//*[@id="container"]/section/div[1]/div').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="qsh-chexing-rest-brand-7"]/div').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="qsh-chexing-rest-model-44"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="qsh-chexing-rest-year-2010"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div/div/div[1]').click()
        time.sleep(2)
        carname = self.driver.find_element_by_xpath('//*[@id="container"]/section/div[1]/div').text
        print (u'选择的车型是：%s'%carname)
        # 验证金额是否一致
        # 工时费
        time_fee_1 = re.compile(r'\d+\.\d+').findall(self.driver.find_element_by_xpath('//*[@id="container"]/section/div[2]/div/div[2]/em').text)
        time_fee = float(time_fee_1[0])
        print time_fee
        # 商品总额
        # 商品金额、商品数量
        s = self.driver.find_elements_by_css_selector('#container > section > ul.center > li> div.center-list-price > div.red-font')
        num = self.driver.find_elements_by_css_selector('#container > section > ul.center > li > div.center-list-price > div:nth-child(2)')
        # print num
        #将字符串中的数字提取出来转化为float类型
        def zhuanhua(i):
            goods_fee_1 = re.compile(r'\d+\.?\d*').findall(i.text)
            print goods_fee_1
            goods_fee = float(goods_fee_1[0])
            return  goods_fee
        good_fees = map(zhuanhua,s)
        good_num = map(zhuanhua,num)
        print u"商品列表中的对应商品的价格列表:",good_fees
        print u"商品列表中的对应商品的价格列表:",good_num
        #计算总金额
        total1 = sum(map(lambda (a,b):a*b,zip(good_fees,good_num)))+time_fee
        print (u"总价格:%s"%total1)
        #获取总金额
        total2 = self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[1]/em')
        total = zhuanhua(total2)
        #断言
        self.assertEqual(total1,total)
        # h = driver.current_window_handle
        # print h
        # driver.find_element_by_xpath("//*[@id='jgwab']").click()
        # hs = driver.window_handles
        # print hs
        # driver.switch_to.window(hs[0])e
        # print driver.title
        # driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
        # driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__userName']").send_keys('nanmon1992')
        # driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__password']").send_keys('nanmon19920819')
        # driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__submit']").click()
        time.sleep(3)
        # driver.close()
        if __name__ == "__main__":
            unittest.main()