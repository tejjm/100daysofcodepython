EMAIL = 'johnbeenrecruiting@gmail.com'
PW = 'JohnBeenJohn1996'
INSTA_URL = "https://www.instagram.com/"
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import random

class insta_follower_bot:
    def __init__(self):
        user_data_dir = os.path.join(os.getcwd(),'chrome_profile')
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = '/usr/bin/google-chrome-stable' 
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(version_main=144,options=chrome_options,use_subprocess=True)
    
        
    def login(self):
        self.driver.get(INSTA_URL)
        print("Press Enter to closer browser")
        input()



follower_bot = insta_follower_bot()
follower_bot.login()