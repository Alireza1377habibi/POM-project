from selenium import webdriver
import time
import unittest

class HomePage:

    def __init__(self , driver):
        self.driver = driver
        self.Wellcome_link_text = 'welcome'
        self.Logout_Text_linktest = 'Logout'
    
    def ClickWelcome(self):
        self.driver.find_element_by_id(self.Wellcome_link_text).click()

    def ClickLogout(self):
        self.driver.find_element_by_link_text(self.Logout_Text_linktest).click()
        
