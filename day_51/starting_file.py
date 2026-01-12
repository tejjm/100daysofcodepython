PROMISED_DOWNLOAD = 45
PROMISED_UPLOAD = 45
EMAIL = 'johnbeenrecruiting@gmail.com'
PW = 'Testing@1990'
CHROME_DRIVER_PATH = 'Users/uttej/Development/chromedriver'
URL = 'https://x.com/home'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time



chrome_options = webdriver.ChromeOptions()
user_data_dir = os.path.join(os.getcwd(),'chrome_profile')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument(f'--user-data-dir-{user_data_dir}')
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
time.sleep(1)
enter_email = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
enter_email.send_keys(EMAIL)
time.sleep(2)
next = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')))
next.click()