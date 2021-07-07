import setup as c
import data as d 
from time import sleep
from pprint import pprint
from selenium.webdriver.common.keys import Keys

class Script(c.Setup):
    def __init__(self):
        super().__init__()
    #find the group to navigate
    def get_group(self):
        self.run()
        sleep(8)
        self.driver.get(d.group_name)
        #send mensage to the user menber
    def scroll_down(self):
        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    def get_user(self):
        self.get_group()
        #self.member_id()
        #js_script = "window.open('https://www.facebook.com')"
        #self.driver.execute_script(js_script)

class_script = Script()
class_script.get_user()
