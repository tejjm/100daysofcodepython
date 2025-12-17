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
time.sleep(2)
english.click()
time.sleep(2)
cookie = driver.find_element(By.ID,"bigCookie")
time.sleep(3)
main_duration = 15
main_start = time.time()
while time.time()-main_start < main_duration:
    cookie.click()
        # cookies =  int(driver.find_element(By.ID,"cookies").text).replace(" cookies","")
p0_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice0"]').text).replace(",",""))
p1_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice1"]').text).replace(",",""))
p2_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice2"]').text).replace(",",""))
p3_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice3"]').text).replace(",",""))
p4_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice4"]').text).replace(",",""))
p5_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice5"]').text).replace(",",""))
p6_price = ((driver.find_element(By.XPATH,'//*[@id="productPrice6"]').text).replace(",",""))

print(p4_price)
print(len(p4_price))
driver.quit()

