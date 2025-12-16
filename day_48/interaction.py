from selenium import webdriver
from selenium.webdriver.common.by import By
URL = "https://en.wikipedia.org/wiki/Main_Page"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
articles = driver.find_element(By.XPATH,'//*[@id="articlecount"]/ul/li[2]/a[1]').text
print(f"Wikipedia has {articles} articles currently")
driver.quit()