from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(executable_path='C:\Program Files\geckodriver.exe')
driver.get('https://buy-in-10-seconds.company.site/search')
time.sleep(5)
checkbox = driver.find_element_by_xpath('//input[@id="checkbox-in_stock"]')
checkbox.click()
searchbox = driver.find_element_by_xpath('//input[@id=""]')
searchbox.send_keys('товар 5')
searchbox.send_keys(Keys.ENTER)