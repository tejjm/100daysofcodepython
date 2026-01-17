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
time.sleep(random.uniform(1.5,4))
# email = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
# for character in EMAIL:
#     email.send_keys(character)
#     time.sleep(random.uniform(0.05,0.18))
# time.sleep(random.uniform(0.8,2.5))

# next_button = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/div/span/span')))
# next_button.click()
# time.sleep(random.uniform(1.5, 3.5))




print("Browser is open. Press Enter in the terminal when you're done...")
input()