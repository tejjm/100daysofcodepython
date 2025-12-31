from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from pprint import pprint
ACCOUNT_EMAIL = "uttejgym@gmail.com"#Dummy values which work for this session
ACCOUNT_PASSWORD = "123123"
URL = "https://appbrewery.github.io/gym/"
#Accessing the web page
chrome_options = webdriver.ChromeOptions()
#Creating chrome profile and storing profile
user_data_dir = os.path.join(os.getcwd(),"chrome_profile")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
#Automating login
login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login-button"]')))
login.click()
enter_email = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="email-input"]')))
enter_email.send_keys(ACCOUNT_EMAIL)
enter_pw = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="password-input"]')))
enter_pw.send_keys(ACCOUNT_PASSWORD)
login_after_credentials = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submit-button"]')))
login_after_credentials.click()
#Grabbing the days from schedule page
booking_info = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__ .Schedule_dayTitle__YBybs')))
booking_text = [booking.text for booking in booking_info]
count = 0
booking_day = "Tuesday"
time = "6:00 PM"
for booking in booking_text:
    count +=1
    if booking_day[:3] in booking:
        index1 = count-1
        text_check = booking
# print(index)
# print(text_check)
#Finding Activity details by time
activities = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__')))[index1]
tuesday_activities = activities.find_elements(By.CSS_SELECTOR,'.ClassCard_cardContent__WGvPp')
tuesday_activities_text = [activity.text for activity in tuesday_activities]
count = 0
for activity in tuesday_activities_text:
    count+=1
    if time in activity:
        index2 = count-1
activities = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__')))[index1]
booking_buttons = activities.find_elements(By.CSS_SELECTOR,'.ClassCard_cardActions__tVZBm')
booking_status=(booking_buttons[index2].text)
date_time = booking_buttons[index2].get_attribute('id')
print(date_time)
#Finding if the status is already booked 
# if booking_status == "Booked":
#     print("Already Booked")
# if booking_status == "Join Waitlist":
#     print(f"Joining waitlist")
#     booking_buttons[index2].click()
# if booking_status == "Book Class":
#     booking_buttons[index2].click()
#     print(f"A class has been booked")
# if booking_status == "Waitlisted":
#     print(f"{booking_status}")