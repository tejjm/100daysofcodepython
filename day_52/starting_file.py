EMAIL = 'johnbeenrecruiting@gmail.com'
PW = 'JohnBeenJohn@1996'
INSTA_URL = "https://www.instagram.com/"
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import random

def random_typer(func,text):
    for letter in text:
        time.sleep(random.uniform(0.10,0.15))
        func(letter)
def do_after_sec(func,sec):
    time.sleep(sec)
    try:
        func()
    except Exception as e:
        print(e)

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
        username = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name="email"]')))
        random_typer(username.send_keys,EMAIL)
        password = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name="pass"]')))
        random_typer(password.send_keys,PW)
        login = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span[style="--x---base-line-clamp-line-height: calc(var(--primary-label-line-height) * 1em); --x-lineHeight: calc(var(--primary-label-line-height) * 1em);"]')))
        login.click()
        profile = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[href="/johnbeenrecruiting/"][role="link"]')))
        profile.click()
        print("Press Enter to closer browser")
        input()



follower_bot = insta_follower_bot()
follower_bot.login()