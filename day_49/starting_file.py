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
# count = 0
# booking_day = "Thursday"
time = "6:00 PM"
# for booking in booking_text:
#     count +=1
#     if booking_day[:3] in booking:
#         index1 = count-1
#         text_check = booking
# print(index1)
# print(text_check)
# #Finding Activity details by time
# activities = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__')))[index1]
# date_time = WebDriverWait(activities,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.Schedule_dayTitle__YBybs')))
# text_dt = [dt.text for dt in date_time] #Date time for displaying o/p
# dt = text_dt[0]
# tuesday_activities = activities.find_elements(By.CSS_SELECTOR,'.ClassCard_cardContent__WGvPp')
# tuesday_activities_text = [activity.text for activity in tuesday_activities]
# count = 0
# for activity in tuesday_activities_text:
#     count+=1
#     if time in activity:
#         index2 = count-1
# activities = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__')))[index1]
# booking_buttons = activities.find_elements(By.CSS_SELECTOR,'.ClassCard_cardActions__tVZBm')
# booking_status=(booking_buttons[index2].text)
# # date_time = booking_buttons[index2].get_attribute('id')
# # print(date_time)#Not printing
# #Finding if the status is already booked 
# booked_count = 0
# waitlist_count = 0
# already_booked_waitlisted = 0
# if booking_status == "Booked":
#     already_booked_waitlisted+=1
# if booking_status == "Join Waitlist":
#     waitlist_count+=1
#     booking_buttons[index2].click()
# if booking_status == "Book Class":
#     booking_buttons[index2].click()
#     booked_count+=1
# if booking_status == "Waitlisted":
#     already_booked_waitlisted+=1

# print("--- BOOKING SUMMARY ---")
# print(f"Classes booked : {booked_count}")
# print(f"Already booked/waitlisted : {already_booked_waitlisted}")
# print(f"Total Tuesday 6pm classes processed: {booked_count+waitlist_count+already_booked_waitlisted}\n")

#Booking all classes on Tuesday and Thursday at 18:00
booking_days = ["Tuesday","Thursday"]
day_indexes = []
tc = []
time = "6:00 PM"
for bd in booking_days:
    count = 0
    for booking in booking_text:
        count+=1
        if bd[:3] in booking:
            index1 = count-1
            text_check = booking
            print(day_indexes)
            day_indexes.append(index1)
            tc.append(text_check)
activities = [] #Saving actvity element of Tuesday and Thursday
info_index = []
for index in day_indexes:
    activity = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__')))[index]
    activities.append(activity)
    date_time = WebDriverWait(activity,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.Schedule_dayTitle__YBybs')))
    dt_text = [dt.text for dt in date_time]
    dt = dt_text[0]
    current_activities = activity.find_elements(By.CSS_SELECTOR,'.ClassCard_cardContent__WGvPp')
    current_activities_text = [activity.text for activity in current_activities]
    count = 0
    for activity in current_activities_text:
        count+=1
        if time in activity:
            index2 = count-1
            info_index.append(index2)
booked_count = 0
waitlist_count = 0
already_booked_waitlisted = 0
for activity in activities:
    booking_buttons = activity.find_elements(By.CSS_SELECTOR,'.ClassCard_cardActions__tVZBm')
    booking_status=(booking_buttons[4].text)
    date_time = booking_buttons[4].get_attribute('id')
#Finding if the status is already booked 

    if booking_status == "Booked":
        already_booked_waitlisted+=1
    if booking_status == "Join Waitlist":
        waitlist_count+=1
        booking_buttons[index2].click()
    if booking_status == "Book Class":
        booking_buttons[index2].click()
        booked_count+=1
    if booking_status == "Waitlisted":
        already_booked_waitlisted+=1


print("--- BOOKING SUMMARY ---")
print(f"Classes booked : {booked_count}")
print(f"Already booked/waitlisted : {already_booked_waitlisted}")
print(f"Total Tuesday 6pm classes processed: {booked_count+waitlist_count+already_booked_waitlisted}\n")