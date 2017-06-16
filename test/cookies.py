# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://m.8673h.com")
print len(driver.get_cookies())
try:
       if len(driver.get_cookies()) != 4:
              e = "登陆失败1222"
              raise e
except e:
       print "登陆失败"
len(driver.get_cookies()) == 1
# driver.find_element_by_xpath("//*[@id='container']/div[2]/div[1]/div/div[2]/span").click()
# driver.find_element_by_id("loginname1").send_keys('13456620218')
# driver.find_element_by_id('code1').send_keys('123456')
# driver.find_element_by_id('tcode1').click()
# time.sleep(3)
# print driver.get_cookies()
# driver.delete_cookie(name='cookie_uuid')
# driver.refresh()
# time.sleep(2)
# 在cookies中添加cookie_uuid，直接登陆
# c1 = {u'domain': u'192.168.2.4',
#        u'secure': False,
#        u'value': u'f822eb296b016444f28d04d08a55b5a5df627b0ace06276246df1ce3fac62a4643ad3ccd539cd096cd17a2fb5c6bdcf92ffd84276ff44d401ccedfd6d29495a1c72e5a8d7a8d9e3206bb2c9aacc9c5b55ad0c7718bbfe0351f106463180faea5335d7b988fe532d5943990f6eef09931f8871a941b58dc80edfded7b95f454ab2ba369ac9d8372cfa45e5ef4e224fbf9',
#        u'expiry': 1583917791, u'path': u'/', u'httpOnly': False, u'name': u'cookie_uuid'}
# driver.add_cookie(c1)
# # driver.add_cookie(c2)
# # driver.add_cookie(c3)
# print driver.get_cookies()
time.sleep(3)
driver.refresh()
# print driver.get_cookies()

# [{u'domain': u'192.168.2.4',
#   u'secure': False,
#   u'value': u'1497514248',
#   u'expiry': 1529050248,
#   u'path': u'/',
#   u'httpOnly': False,
#   u'name': u'Hm_lvt_6e13a2e56b664af0685f30e822b2db83'}
#  {u'domain': u'192.168.2.4',
#   u'secure': False,
#   u'value': u'ab69ca7b2f8f1f46dfbf527b39f4f0bcec28e2d87597d75547a3f9fdd3f12ffd919d9b667a19e4bdfaaf63c84ee4cda7cbda7479f3772f438e05819564a3df70aead916e50b00489c3e6c75a86bacb190d7a1ec23a35df6237efb86b8e41adbe335d7b988fe532d5943990f6eef09931f8871a941b58dc80edfded7b95f454ab2ba369ac9d8372cfa45e5ef4e224fbf9',
#   u'expiry': 1583914249,
#   u'path': u'/',
#   u'httpOnly': False,
#   u'name': u'cookie_uuid'},
#  {u'domain': u'192.168.2.4',
#   u'secure': False,
#   u'value': u'1497514248',
#   u'expiry': 1529050249,
#   u'path': u'/',
#   u'httpOnly': False,
#   u'name': u'Hm_lvt_6e13a2e56b664af0685f30e822b2db83'}]