from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
URL = "https://www.python.org/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
# price = driver.find_element(By.XPATH,value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]').text
# print(f"The shirts price today is {price}")
events_list = driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
pprint(events_list)
driver.quit()