# -*- coding: utf-8 -*-
from turtle import title

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import scrapy



class FlightsSpider(scrapy.Spider):
    name = "flights"
    allowed_domains = ["justfly.com"]
    start_urls = [
        'https://www.justfly.com/',
    ]

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'd:\geckodriver.exe')
        



    def parse(self, response):
                
        self.driver.get(response.url)
        login_form = self.driver.find_element_by_name('air_search_form')
        fromAPT = self.driver.find_element_by_name('seg0_from')
        toAPT = self.driver.find_element_by_name('seg0_to')
        fromDate = self.driver.find_element_by_name('seg0_date')
        toDate = self.driver.find_element_by_name('seg1_date')
        fromAPT.send_keys("DEL")
        toAPT.send_keys("GOI")
        fromDate.click()
        m = self.driver.find_elements_by_class_name("ui-datepicker-calendar")        
        print('Working On Date')
        print(type(m))
        for i in m:
            print('Element Start -- \t')
            print(i)        
            print('Element END--- \t')    
            if i.text.find() == "27":
                print("Working to cllllllllllllll")
                i.click()
                break

        toDate.click()
        print('Working On Date2')
        m = self.driver.find_elements_by_class_name("ui-datepicker-calendar")        
        for i in m:
            #verify required date then click
            if i.text is '29':
                i.click()
            break
#get selected date
        # fromDate.send_keys("01012011")
       
       
       
        actions = ActionChains(self.driver)
        actions.click(commit)
        actions.perform()
      
        time.sleep(3)
        self.driver.close()
