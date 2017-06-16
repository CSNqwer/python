class Login(object):
    def login(self,driver, username, password):
        driver.find_element_by_xpath("//*[@id='container']/div[2]/div[1]/div/div[2]/span").click()
        driver.find_element_by_id("loginname1").send_keys(username)
        driver.find_element_by_id('code1').send_keys(password)
        driver.find_element_by_id('tcode1').click()