import time
from selenium import webdriver
driver= webdriver.Chrome()
driver.get('https://www.facebook.com/') 
print(driver.title)
print(driver.current_url)
time.sleep(3)
driver.close()