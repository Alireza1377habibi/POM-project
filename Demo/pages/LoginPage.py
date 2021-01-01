from selenium import webdriver
import time
import unittest

class LoginPage :

    def __init__(self , driver):

        self.driver = driver
        self.username_Text_id = 'txtUsername'
        self.password_Text_id = 'txtPassword'
        self.click_Text_id = 'btnLogin'

    def EnterUsername(self , username):
        
        self.driver.find_element_by_id(self.username_Text_id).send_keys(username)

    def EnterPassWord(self , password):

        self.driver.find_element_by_id(self.password_Text_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element_by_id(self.click_Text_id).click()

    


    