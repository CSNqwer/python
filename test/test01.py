# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# 用chrome的Mobile emulation模拟手机浏览器测试手机网页
WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; SM-G9280 Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.5) WindVane/8.0.0 1440X2560 GCanvas/1.4.2.21'
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome( chrome_options=options)
driver.set_window_size(338,740)
driver.get('http://m.8673h.com')

# url = "http://www.baidu.com"
# driver = webdriver.Chrome()
# driver.get(url)
# time.sleep(3)
# # driver.implicitly_wait(10)
# builder = ActionChains(driver)
# builder.key_down(Keys.F12).perform()
# driver.maximize_window()
# mouse = driver.find_element_by_xpath("//*[@id='u1']/a[8]")
# ActionChains(driver).move_to_element(mouse).perform()
# ActionChains(driver).context_click().perform()
# driver.find_element_by_xpath("//*[@id='kw']").send_keys(u"selenium 自动化测试")
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'x')
# driver.find_element_by_xpath("//*[@id='kw']").send_keys(u"selenium 自动化测试 uinttest")
# driver.find_element_by_css_selector("#su").send_keys(Keys.ENTER)
# time.sleep(1)
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys(u"葫芦娃")
# time.sleep(3)
# driver.get("http://cn.bing.com/")
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
time.sleep(3)
# driver.close()
