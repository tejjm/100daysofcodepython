from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
URL = "https://ozh.github.io/cookieclicker/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(2)
english = driver.find_element(By.XPATH,'//*[@id="langSelect-EN"]')
time.sleep(3)
english.click()
time.sleep(3)
cookie = driver.find_element(By.ID,"bigCookie")
time.sleep(5)
for n in range(0,100):
    cookie.click()

driver.quit()