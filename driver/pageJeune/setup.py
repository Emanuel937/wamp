from selenium import webdriver
import data as info
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import xlsxwriter

class Goto():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\Le Graal Auto EA\AppData\Local\Programs\Python\Python38\Lib\site-packages\selenium\geckodriver.exe")
        self.driver.get(info.url)
        #creat excel file 
        self.workbook = xlsxwriter.Workbook(info.file_name)
        self.worksheet = self.workbook.add_worksheet()
        #the fisrt line
        self.worksheet.write('A1', 'Name')
        self.worksheet.write('B1', 'Tel')
        self.worksheet.write('C1', 'Job')
        self.worksheet.write('D1', 'address')
        self.worksheet.write('E1', 'site')
        #end
        self.celulas = 2
        #postal 
        self.start = 75
        self.end =76

    def  acceptCookies(self):
        button = self.driver.find_element_by_id("didomi-notice-agree-button")
        button.click()

    def searchFor(self, postalCity):
        try:
            need =  self.driver.find_element_by_id("quoiqui")
            need.clear()
            need.send_keys(info.searchFor)
            #wait 
            sleep(1)
            city = self.driver.find_element_by_id("ou")
            city.clear()
            city.send_keys(postalCity)
            #start search then 
            sleep(1)
            runSearch = self.driver.find_element_by_css_selector("button[title='Trouver']")
            runSearch.click()
        except:
            self.workbook.close()
        
    def notSite(self, element_len):
        self.getData(element_len)

    def getData(self, element_len):
        try:
            parent = self.driver.find_elements_by_css_selector(".bi-bloc.blocs")[element_len]
            #get only the user that don't have website
            #the end
            try:
                centerName =  parent.find_element_by_css_selector(".denomination-links.pj-link").text
            except:
                centerName ="pas "
            #get the number phone
            try:
                btn_num = parent.find_element_by_css_selector(".icon.icon-phone")
                btn_num.click()
                try:
                    tel = parent.find_elements_by_class_name("num")
                    texts = []
                    for matched_element in tel:
                        text = matched_element.text
                        texts.append(text)
                        
                    tel = texts[0]
                    print(tel)
                except:
                    tel = "pas de numero tel"
                    
            except:
                tel = "pas tel"

            #job title
            try :
                jobTitle = parent.find_element_by_css_selector(".activites.pj-lb.pj-link").text
            except:
                jobTitle ="pas domaine"   
            try:
                address = parent.find_element_by_css_selector(".adresse.pj-lb.pj-link").text
                address = address.split(",")
                address = address[0] + ","+ address[1]
            except:
                address =" pas address"
            
            try:
                site = parent.find_element_by_xpath('.//a[contains(text(), "internet")]')
                site = "ok"
            except:
                site = "vide"
        except:
            pass
        
        #fill the excel file
        self.worksheet.write("A{}".format(self.celulas), centerName)
        self.worksheet.write("B{}".format(self.celulas), tel)
        self.worksheet.write("C{}".format(self.celulas),  jobTitle)
        self.worksheet.write("D{}".format(self.celulas), address)
        self.worksheet.write("E{}".format(self.celulas), site)
        
        self.celulas += 1

        
    def getAllElement(self):
        try:
            allElements = self.driver.find_elements_by_css_selector(".bi-bloc.blocs")
            res =  len(allElements) -1
            inicilize = 0
            while(True):
                 #call getdata function
                 self.notSite(inicilize)
                 #sleep(2) 
              
                 if res == inicilize:
                     self.nextPage()
                     break
                 inicilize +=1
        except:
            res = "nothing"  

    def nextPage(self):
        
        try:
            while(self.driver.find_element_by_id("pagination-next")):
                #go to next
                next = self.driver.find_element_by_id("pagination-next")
                #sleep(1)
                next.click()
                #call the getAllElement function 
                self.getAllElement()
                
        except :
            if self.start == self.end:
                #self.workbook.close()
                print("gooo")
            res ="end"
            print(res)
          
    def get_from_all_france(self):
        try:
            self.driver.find_element_by_xpath('.//h1[contains(text(), "Sécurité")]')
            self.workbook.close()
        except:
            self.acceptCookies()
            #start is the first code postal :01
            while(True):
                    if self.start < 10:
                        start_string = "0{}".format(self.start)
                    else:
                        start_string = str(self.start)

                    self.searchFor(start_string)
                    sleep(2)
                    self.getAllElement()
                    if self.start == self.end:
                        self.workbook.close()
                        sleep(1)
                        break
                    self.start += 1


    def run(self):
        #wait  a bit before send the keys
        #self.driver.add_cookie({"name":"hc_accessibility", "value":"9iUH38K+vvAWGVQADqVcKDwskybHHTRX0v5G0pNzAFNeTxea5k9RU0IWSyRIQFCOoK26fEiaRc6E8EUcyOnrsftz9G54JYCKzTAFdYFqKgJL6nYc5lXt7pwfznY7lut+2hZoFeFqTLty+fDQvese/QOoAIr1xd3mqRuH1yMIBcurEv1a/QOTvlumv6Aza7dV0PE3NHI5YhNCAQ7H1P5WrCtGoAP6UVAY8AQwBAOI1JydiNVdggf22ieTc9QUZv8kmzarKYZ8VAaGk5yIy3VYDIflKGKBgfcovS+UDjnZUw38HoY484MhpdniVpeR6/n3cY//mQb9FPDgSjarSD2NLigjrrJU7bkMqVCVkWgESCPWIrvoDrX+D4XLoB/aQghIE6VLx0NrH7jUlV+8BOPBslHO25iEQ14SczMymv5Bs2+ygf0SlvV/vtalpTON/IKm1axqm7zf97Mk/Mjg"})
        #self.driver.add_cookie({"name":"session", "value":"cea7ddb6-1e42-47db-b881-233fe7cb08cf"})
        
        #self.driver.get(info.url)
        #sleep(1000) 
        sleep(1)
        self.get_from_all_france()
        
        
varGo = Goto()
varGo.run()