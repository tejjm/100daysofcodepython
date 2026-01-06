from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver,ACCOUNT_EMAIL,ACCOUNT_PASSWORD,URL):
    try:
        driver.set_page_load_timeout(15)
        driver.get(URL)
        login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-button"]')))
        login.click()
        enter_email = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="email-input"]')))
        enter_email.send_keys(ACCOUNT_EMAIL)
        enter_pw = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="password-input"]')))
        enter_pw.send_keys(ACCOUNT_PASSWORD)
        submit = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submit-button"]')))
        submit.click()
        time.sleep(2)
        error_elem =driver.find_elements(By.XPATH,'//*[@id="error-message"]') 
        if error_elem:
            raise Exception("Login failed, network issue")
        return True
    except Exception as e:
        raise Exception(f"Login failed : {e}")