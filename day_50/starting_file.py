from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

URL = 'https://tinder.com/'
chrome_options = webdriver.ChromeOptions()
user_data_dir = os.path.join(os.getcwd(),'chrome_profile')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

#Logging in
accept = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c1649373191"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')))
accept.click()