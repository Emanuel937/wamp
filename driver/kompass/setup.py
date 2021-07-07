from selenium import webdriver
import data as info
from time import sleep

class Kompass:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Le Graal Auto EA\AppData\Local\Programs\Python\Python38\Lib\site-packages\selenium\geckodriver.exe")
        self.driver.get(info.url)
        self.sector_index = False
        self.sector_init  = 0
        self.links_total  = False
        self.links_init   = 0
        self.first_page   = 1
        self_last_page    = 3

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

    def get_secteur(self):
        btn_sector = self.selector("a#headerMenuDirectoryTitleCollapsed")
        btn_sector.click()
        #update the selector_index
        category =  self.selector_all("li a.navSecteurActivityLink")
        self.selector_index =  len(category) -1
        #display block on category clicked ...
        category[self.sector_init].click()
        #get under sector
        arg = "div#secteur-{}".format(self.sector_init)
        parent_of_link =  self.selector(arg)
        #total links
        links_total =  parent_of_link.find_elements_by_css_selector("ul li a")
        self.links_total = len(links_total) -1 
        links_total[self.links_init].click()
        
        '''while True:
            links_total[self.links_init].click()
            if(self.links_total == self.links_init):
                #change the category ...
                print("game over")
                break

            self.links_init += 1
            sleep(3)'''
       
    def make_excel_database(self):
        pass
    
    def next(self):
        while True:
            self.get_secteur()
            if(self.first_page == self.last_page):
                break
            self.first_page +=1
            
    def brain_app(self):
        #here come the logic of application
        while True:
            if(self.selector_init == self.selector_index):
                break
        self.index_init += 1

    def run(self):
        self.get_secteur()

class_name = Kompass()
class_name.run()
