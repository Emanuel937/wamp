from selenium import webdriver
import data as d
from time import sleep
class Setup():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Le Graal Auto EA\AppData\Local\Programs\Python\Python38\Lib\site-packages\selenium\geckodriver.exe")
        self.driver.get(d.url)
    # find element 
    def selector(self, parms):
        return self.driver.find_element_by_css_selector(parms)
    def selector_all(self, parms):
        return self.driver.find_elements_by_css_selector(parms)
    # click on the element using the index
    def ex_sc(self, i, element):
        args = "arguments[{}].click();"
        args = args.format(i)
        return self.driver.execute_script(args,element)
    def login(self):
        #input email
        user_email = self.selector(d.loginCss['email'])
        user_email.clear()
        user_email.send_keys(d.email)
        #input password
        user_pass = self.selector(d.loginCss['pass'])
        user_pass.clear()
        user_pass.send_keys(d.password)
        #click on button
        btn_login = self.selector(d.loginCss['btn'])
        self.ex_sc(0, btn_login)
        sleep(8)
        #accept the cookies
        btn_cookies = self.selector(d.cookies_btn)
        self.ex_sc(0, btn_cookies)
    def run(self):
        self.login()



