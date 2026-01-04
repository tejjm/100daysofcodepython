from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login
from retry_func import retry
import os
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
success = retry(lambda:login(driver,ACCOUNT_EMAIL,ACCOUNT_PASSWORD),delay=2,description="Login to Gym")
if not success:
    print("Failed to login")
    driver.quit()

# #Grabbing the days from schedule page
# booking_info = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__ .Schedule_dayTitle__YBybs')))
# booking_text = [booking.text for booking in booking_info]
# # count = 0
# # booking_day = "Thursday"
# time = "6:00 PM"
# #Booking all classes on Tuesday and Thursday at 18:00
# booking_days = ["Tuesday","Thursday"]
# day_indexes = []
# tc = []
# time = "6:00 PM"
# for bd in booking_days:
#     count = 0
#     for booking in booking_text:
#         count+=1
#         if bd[:3] in booking:
#             index1 = count-1
#             text_check = booking
#             day_indexes.append(index1)
#             tc.append(text_check)
# activities = [] #Saving actvity element of Tuesday and Thursday
# info_index = []
# for index in day_indexes:
#     activity = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__')))[index]
#     activities.append(activity)
#     date_time = WebDriverWait(activity,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.Schedule_dayTitle__YBybs')))
#     dt_text = [dt.text for dt in date_time]
#     dt = dt_text[0]
#     current_activities = activity.find_elements(By.CSS_SELECTOR,'.ClassCard_cardContent__WGvPp')
#     current_activities_text = [activity.text for activity in current_activities]
#     count = 0
#     for activity in current_activities_text:
#         count+=1
#         if time in activity:
#             index2 = count-1
#             info_index.append(index2)
# booked_count = 0
# waitlist_count = 0
# already_booked_waitlisted = 0
# for activity in activities:
#     booking_buttons = activity.find_elements(By.CSS_SELECTOR,'.ClassCard_cardActions__tVZBm')
#     booking_status=(booking_buttons[4].text)
#     date_time = booking_buttons[4].get_attribute('id')
# #Finding if the status is already booked 

#     if booking_status == "Booked":
#         already_booked_waitlisted+=1
#     if booking_status == "Join Waitlist":
#         waitlist_count+=1
#         booking_buttons[index2].click()
#     if booking_status == "Book Class":
#         booking_buttons[index2].click()
#         booked_count+=1
#     if booking_status == "Waitlisted":
#         already_booked_waitlisted+=1


# #Verifying booking confirmed, waitlist joined
# my_bookings = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="my-bookings-link"]')))
# my_bookings.click()
# bookings = WebDriverWait(driver, 15).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.MyBookings_bookingDetails__QG0l_')))
# number_of_bookings = len(bookings)

# print("--- BOOKING SUMMARY ---\n")
# print(f"Classes booked : {booked_count}")
# print(f"Already booked/waitlisted : {already_booked_waitlisted}")
# print(f"Total classes processed: {booked_count+waitlist_count+already_booked_waitlisted}\n")
# print("--- VERIFYING ON MY BOOKINGS PAGE ---\n")
# print(f"Verified bookings : {number_of_bookings}\n")
# verified_bookings_text = [vb.text for vb in bookings]
# if verified_bookings_text:
#     sno=0
#     for text in verified_bookings_text:
#         sno+=1
#         print(f"{sno}. {text}")
#         print('\n')
# if number_of_bookings==booked_count+waitlist_count:
#     print(f"Verification matched")
#     print(f"Booked/Waitlist joined ={booked_count+waitlist_count}")
#     print(f"Verified count = {number_of_bookings}")

