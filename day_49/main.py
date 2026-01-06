from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from login import login
from booking import book_class
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

#Automating login
success = retry(lambda:login(driver,ACCOUNT_EMAIL,ACCOUNT_PASSWORD,URL),delay=2,description="Login to Gym")
if not success:
    print("Failed to login")
    driver.quit()

# #Grabbing the days from schedule page
counts = retry(lambda:book_class(driver),delay=2,description="booking classes")


#Verifying booking confirmed, waitlist joined
my_bookings = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="my-bookings-link"]')))
my_bookings.click()
bookings = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.MyBookings_bookingDetails__QG0l_')))
number_of_bookings = len(bookings)

print("--- BOOKING SUMMARY ---\n")
print(f"Classes booked : {counts[0]+counts[1]}")
print(f"Already booked/waitlisted : {counts[2]}")
print(f"Total classes processed: {counts[0]+counts[1]+counts[2]}\n")
print("--- VERIFYING ON MY BOOKINGS PAGE ---\n")
print(f"Verified bookings : {number_of_bookings}\n")
verified_bookings_text = [vb.text for vb in bookings]
if verified_bookings_text:
    sno=0
    for text in verified_bookings_text:
        sno+=1
        print(f"{sno}. {text}")
        print('\n')
if number_of_bookings==counts[0]+counts[1]+counts[2]:
    print(f"Verification matched")
    print(f"Booked/Waitlist joined ={counts[0]+counts[1]+counts[2]}")
    print(f"Verified count = {number_of_bookings}")

