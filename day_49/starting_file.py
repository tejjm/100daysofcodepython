from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from pprint import pprint
ACCOUNT_EMAIL = "uttejgym@gmail.com"#Dummy values which work for this session
ACCOUNT_PASSWORD = "123123"
URL = "https://appbrewery.github.io/gym/"
#Accessing the web page
chrome_options = webdriver.ChromeOptions()
#Creating chrome profile and storing profile
user_data_dir = os.path.join(os.getcwd(),"chrome_profile")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
#Automating login
login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-button"]')))
login.click()
enter_email = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="email-input"]')))
enter_email.send_keys(ACCOUNT_EMAIL)
enter_pw = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="password-input"]')))
enter_pw.send_keys(ACCOUNT_PASSWORD)
login_after_credentials = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submit-button"]')))
login_after_credentials.click()
#Grabbing the days from schedule page
booking_info = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__ .Schedule_dayTitle__YBybs')))
booking_text = [booking.text for booking in booking_info]
count = 0
booking_day = "Tuesday"
for booking in booking_text:
    count +=1
    if booking_day[:3] in booking:
        index = count-1
        text_check = booking
print(index)
print(text_check)
