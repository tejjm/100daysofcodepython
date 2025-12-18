from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
URL = "https://ozh.github.io/cookieclicker/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(2)
english = driver.find_element(By.XPATH,'//*[@id="langSelect-EN"]')
time.sleep(2)
english.click()
time.sleep(2)
cookie = driver.find_element(By.ID,"bigCookie")
time.sleep(1)

main_duration = 20
main_start = time.time()
while time.time()-main_start < main_duration:
    check = time.time()
    check_duration = 5
    while time.time()-check < check_duration:
        #Clicks on cookie for 5 secs
        cookie.click()
    p0_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice0"]').text).replace(",",""))
    p1_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice1"]').text).replace(",",""))
    p2_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice2"]').text).replace(",",""))
    p3_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice3"]').text).replace(",",""))
    p4_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice4"]').text).replace(",",""))
    p5_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice5"]').text).replace(",",""))
    p6_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice6"]').text).replace(",",""))
    cookies_text = (driver.find_element(By.XPATH,'//*[@id="cookies"]').text).replace(",","")
    cookies = re.match(r'\d+',cookies_text).group() if re.match(r'\d+',cookies_text) else None
    print(cookies)
    # #Buying with cookies
    if p6_price:
        while int(p6_price) < int(cookies):
            driver.find_element(By.XPATH,'//*[@id="product6"]').click()
    if p5_price:
        while int(p5_price) < int(cookies):
            driver.find_element(By.XPATH,'//*[@id="product5"]').click()
    if p4_price:
        while int(p4_price) < int(cookies):
            driver.find_element(By.XPATH,'//*[@id="product4"]').click()
    if p3_price:
        while int(p3_price) < int(cookies):
            driver.find_element(By.XPATH,'//*[@id="product3"]').click()
    if p2_price:
        while int(p2_price) < int(cookies):
            driver.find_element(By.XPATH,'//*[@id="product2"]').click()
    if p1_price:
        while int(p1_price) < int(cookies):
            driver.find_element(By.XPATH,'//*[@id="product1"]').click()
    if p0_price:
        while int(p0_price) < int(cookies):
            driver.find_element(By.XPATH,'//*[@id="product0"]').click()
        print("Clicked p0")
driver.quit()

