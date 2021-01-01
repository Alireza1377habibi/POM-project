from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
time.sleep(2)
driver.find_element_by_id('btnLogin').click()
time.sleep(2)
driver.find_element_by_id('welcome').click()
time.sleep(3)
driver.find_element_by_tag_name('b').click()
time.sleep(10)
driver.close()
driver.quit()

