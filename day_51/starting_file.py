PROMISED_DOWNLOAD = 45
PROMISED_UPLOAD = 45
EMAIL = 'johnbeenrecruiting@gmail.com'
PW = 'Testing@1990'
CHROME_DRIVER_PATH = 'Users/uttej/Development/chromedriver'
URL = 'https://x.com/home'
from selenium import webdriver
import os



chrome_options = webdriver.ChromeOptions()
user_data_dir = os.path.join(os.getcwd(),'chrome_profile')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument(f'--user-data-dir-{user_data_dir}')
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

