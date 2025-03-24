from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
url1='https://www.google.com/'
driver.get(url1)
driver.maximize_window()
driver.implicitly_wait(10)
element1=driver.find_element(By.NAME,'q')
element1.send_keys('hello')
element1.submit()
driver.close()