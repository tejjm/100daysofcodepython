from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

URL = 'https://tinder.com/'
chrome_options = webdriver.ChromeOptions()
user_data_dir = os.path.join(os.getcwd(),'chrome_profile')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

#Logging in
# accept = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c1649373191"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')))
# accept.click()

try:
    login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c1649373191"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/header/div/div[2]/div[2]/a/div[2]/div[2]/div')))
    login.click()
    login_with_fb = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c-79007885"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')))
    login_with_fb.click()
    print(driver.title)
    base = driver.current_window_handle
    time.sleep(3)
    handles = set(driver.window_handles)
    if len(handles) > 1:
        fb_window = (handles-{base}).pop()
        driver.switch_to.window(fb_window)
        print(driver.title)
        continue_as_u = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[@role='button' and starts-with(@aria-label,'Continue as')]")))
        continue_as_u.click()
    driver.switch_to.window(base)
    print(print(driver.title))
except Exception:
    print("Passing")
    pass

like_xpath = '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]'
swipe = True
like_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,like_xpath)))
count = 0
while swipe:
    try:
        pop_up1 = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c-79007885"]/div/div/div[1]')))
        pop_up1.click()
        break
        
    except Exception:
        pass
    like_button.click()
    time.sleep(2)
    print(f"Swiping done {count} times")

profile = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c1649373191"]/div/div[1]/div/aside/nav/a')))
profile.click()
like_button = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c1649373191"]/div/div[1]/div/aside/nav[2]/div/div/div/div/div/div/div[20]')))
# driver.quit()
