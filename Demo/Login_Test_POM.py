from selenium import webdriver
import time
import unittest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def Test_LoginValid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        
        Login = LoginPage(driver)
        Login.EnterUsername('admin')
        time.sleep(3)
        Login.EnterPassWord('admin123')
        time.sleep(2)
        Login.ClickLogin()

        hemepage = HomePage(driver)
        time.sleep(3)
        homepage.ClickWelcome()
        time.sleep(3)
        hemepage.ClickLogout()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
