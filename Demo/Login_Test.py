from selenium import webdriver
import time
import unittest

class LoginTest (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def Test_LoginValid(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        time.sleep(2)
        self.driver.find_element_by_id('btnLogin').click()
        time.sleep(5)
        self.driver.find_element_by_id('welcome').click()
        time.sleep(3)
        self.driver.find_element_by_tag_name('a').click()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

