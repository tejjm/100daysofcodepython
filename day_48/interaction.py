from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
URL = "https://secure-retreat-92358.herokuapp.com/"
FIRST_NAME = "Uttej"
LAST_NAME = "Bankai"
EMAIL = "bankaibankai@bankai.com"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
fname = driver.find_element(By.XPATH,"/html/body/form/input[1]")
lname = driver.find_element(By.XPATH,"/html/body/form/input[2]")
email_ = driver.find_element(By.XPATH,"/html/body/form/input[3]")
fname.send_keys(FIRST_NAME,Keys.ENTER)
lname.send_keys(LAST_NAME,Keys.ENTER)
email_.send_keys(EMAIL,Keys.ENTER)
sign_up = driver.find_element(By.XPATH,"/html/body/form/button")
sign_up.click()

# driver.quit()