# -*- coding: utf-8 -*-
from datetime import date
from turtle import title

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import scrapy

# https://www.justfly.com/flight/search?num_adults=1&num_children=0&num_infants=0&num_infants_lap=0&seat_class=Economy&seg0_date=2022-03-30&seg0_from=DEL&seg0_to=GOI&seg1_date=2022-07-11&seg1_from=GOI&seg1_to=DEL&type=roundtrip

class FlightsSpider(scrapy.Spider):
    name = "flights"
    allowed_domains = ["justfly.com"]
    start_urls = [
        'https://www.justfly.com/flight/search?num_adults=1&num_children=0&num_infants=0&num_infants_lap=0&seat_class=Economy&seg0_date=2022-03-30&seg0_from=DEL&seg0_to=GOI&seg1_date=2022-07-11&seg1_from=GOI&seg1_to=DEL&type=roundtrip',
    ]

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'd:\geckodriver.exe')
        
    def parse(self, response):  
        self.driver.get(response.url)
        /html/body/div[2]/div[8]/div/div[4]/div/div/div[2]/div[3]/div[2]/div/ul/li[1]/div[1]/div[1]/div[1]/div/span[1]/span[1]
        /html/body/div[2]/div[8]/div/div[4]/div/div/div[2]/div[3]/div[2]/div/ul/li[1]/div[1]/div[1]/div[1]/div/span[1]/span[3]
        /html/body/div[2]/div[8]/div/div[4]/div/div/div[2]/div[3]/div[2]/div/ul/li[1]/div[1]/div[1]/div[1]/div/span[1]/span[1]
        
#         login_form = self.driver.find_element_by_name('air_search_form')
#         fromAPT = self.driver.find_element_by_name('seg0_from')
#         toAPT = self.driver.find_element_by_name('seg0_to')
#         fromDate = self.driver.find_element_by_name('seg0_date')
#         toDate = self.driver.find_element_by_id('date-picker-2')
#         fromAPT.send_keys("DEL")
#         toAPT.send_keys("GOI")
#         fromDate.click()
#         #m = self.driver.find_elements_by_class_name("ui-datepicker-calendar")        
#         dateFro = self.driver.find_element_by_xpath("/html/body/div[16]/div[1]/table/tbody/tr[5]/td[4]/a")        
        
#         dateFro.click()

# #        toDate.click()
                                           
#         dateto = self.driver.find_element_by_xpath("/html/body/div[16]/div[1]/table/tbody/tr[2]/td[2]/a")
#         print('from date element {0} Data Type {1}  Text {2} '.format(dateto,type(dateto), dateto.text))
#         dateto.click()
        # /html/body/div[16]/div[1]/table/tbody/tr[5]/td[4]/a

            

        # tr count 
        # td count 

        # print('Working On Date')
        # print(type(m))
        # for i in m:
        #     print('Element Start -- \t')
        #     print(i)        
        #     print('Element END--- \t')    
        #     if i.text.find() == "29":
        #         print("Working to cllllllllllllll")
        #         i.click()
        #         break

        # toDate.click()
        # print('Working On Date2')
        # m = self.driver.find_elements_by_class_name("ui-datepicker-calendar")        
        # for i in m:
        #     #verify required date then click
        #     if i.text is '29':
        #         i.click()
        #     break
#get selected date
        # fromDate.send_keys("01012011")
       
       
       
        actions = ActionChains(self.driver)
        actions.click(commit)
        actions.perform()
      
        time.sleep(3)
        self.driver.close()
