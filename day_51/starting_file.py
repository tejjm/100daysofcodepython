PROMISED_DOWNLOAD = 45
PROMISED_UPLOAD = 45
EMAIL = 'johnbeenrecruiting@gmail.com'
PW = 'Testing@1990'
URL = 'https://bsky.app/'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import os
import time
import random


user_data_dir = os.path.join(os.getcwd(),'chrome_profile')
chrome_options = uc.ChromeOptions()
chrome_options.binary_location = '/usr/bin/google-chrome-stable' 
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_experimental_option('detach',True)
driver = uc.Chrome(options=chrome_options,use_subprocess=True)
driver.get(url=URL)
time.sleep(random.uniform(1.5,2.8))
signin = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/button/span')))
signin.click()
time.sleep(random.uniform(1.5,2.8))
email = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/input')))
for character in EMAIL:
    email.send_keys(character)
    time.sleep(random.uniform(0.05,0.18))
time.sleep(random.uniform(0.8,2.5))

password = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/input')))
for character in PW:
    password.send_keys(character)
    time.sleep(random.uniform(0.05,0.18))
time.sleep(random.uniform(0.8,2.5))

next_button = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/button[2]')))
next_button.click()
time.sleep(random.uniform(1.5, 3.5))




print("Browser is open. Press Enter in the terminal when you're done...")
input()