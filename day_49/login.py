from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver,ACCOUNT_EMAIL,ACCOUNT_PASSWORD):
    login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-button"]')))
    login.click()
    enter_email = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="email-input"]')))
    enter_email.send_keys(ACCOUNT_EMAIL)
    enter_pw = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="password-input"]')))
    enter_pw.send_keys(ACCOUNT_PASSWORD)
    login_after_credentials = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submit-button"]')))
    login_after_credentials.click()