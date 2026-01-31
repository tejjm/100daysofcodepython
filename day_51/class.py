PROMISED_DOWNLOAD = 300
PROMISED_UPLOAD = 300
EMAIL = 'johnbeenrecruiting@gmail.com'
PW = 'Testing@1990'
URL = 'https://bsky.app/'
SPEED_URL = "https://www.speedtest.net/"
DOWNLOAD_CSS = 'span.result-data-large.number.result-data-value.download-speed'
UPLOAD_CSS = 'span.result-data-large.number.result-data-value.upload-speed'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import os
import time
import random


class InternetSpeedTweetBot:
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
        self.up = None
        self.down = None
    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        # sppedtest_go = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[class*="start-button"]')))
        speedtest_go = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')))
        speedtest_go.click()
        time.sleep(30)
        speed_d = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,DOWNLOAD_CSS)))
        time.sleep(30)
        speed_u = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,UPLOAD_CSS)))
        return speed_d,speed_u

    def tweet_at_provider(self,up,down):
        if up < PROMISED_UPLOAD or down < PROMISED_DOWNLOAD:
            self.driver.get(URL)
            new_post = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[aria-label="Compose new post"]')))
            new_post.click()
            type = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[contenteditable="true"][role="textbox"]')))
            message = f"Hey @act my current network speed is  {up} MBPS upload and {down} MBPS download, I was promised {PROMISED_UPLOAD} MBPS upload and {PROMISED_DOWNLOAD} MBPS download, What happened? "
            for n in message:
                time.sleep(random.uniform(0.10,0.25))
                type.send_keys(n)
            post = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[data-testid="composerPublishBtn"]')))
            post.click()
            profile = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[aria-label="Profile"]')))
            profile.click()      
        print("Press Enter to exit browser")
        input()
        


tweet_bot = InternetSpeedTweetBot()
down,up = tweet_bot.get_internet_speed()
down = float(down.text)
up = float(up.text)
tweet_bot.tweet_at_provider(up=up,down=down)
