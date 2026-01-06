from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def book_class(driver,):
    booking_info = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__ .Schedule_dayTitle__YBybs')))
    booking_text = [booking.text for booking in booking_info]
    # count = 0
    # booking_day = "Thursday"
    time = "6:00 PM"
    #Booking all classes on Tuesday and Thursday at 18:00
    booking_days = ["Tuesday","Thursday"]
    day_indexes = []
    tc = []
    time = "6:00 PM"
    for bd in booking_days:
        count = 0
        for booking in booking_text:
            if bd[:3] in booking:
                index1 = count
                text_check = booking
                day_indexes.append(index1)
                tc.append(text_check)
            count+=1
    activities = [] #Saving actvity element of Tuesday and Thursday
    info_index = []
    for index in day_indexes:
        activity = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#schedule-page .Schedule_dayGroup__y79__')))[index]
        activities.append(activity)
        date_time = WebDriverWait(activity,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.Schedule_dayTitle__YBybs')))
        dt_text = [dt.text for dt in date_time]
        dt = dt_text[0]
        current_activities = activity.find_elements(By.CSS_SELECTOR,'.ClassCard_cardHeader__D9pf3 .ClassCard_cardContent__WGvPp')
        current_activities_text = [activity.text for activity in current_activities]
        count = 0
        for activity in current_activities_text:
            if time in activity:
                # print(activity)
                index2 = count
                info_index.append(index2)
            count+=1
    booked_count = 0
    waitlist_count = 0
    already_booked_waitlisted = 0
    # print(info_index)

    for activity in activities:
        n=0
        booking_buttons = activity.find_elements(By.CSS_SELECTOR,'.ClassCard_cardActions__tVZBm')
        print(f"Booking buttons availale {len(booking_buttons)}")
        booking_status=(booking_buttons[info_index[n]].text)
        date_time = booking_buttons[info_index[n]].get_attribute('id')
    # #Finding if the status is already booked 

        if booking_status == "Booked":
            already_booked_waitlisted+=1
        if booking_status == "Join Waitlist":
            try:
                waitlist_count+=1
                print(f"Info index {info_index[n]}")
                print(f"Length of booking index {len(booking_buttons)}")
                booking_buttons[info_index[n]].click()
                time.sleep(2)
                error_elem = driver.find_elements(By.CSS_SELECTOR,'.ClassCard_cardHeader__D9pf3 .ClassCard_errorMessage__Xwjwz')
                if error_elem:
                    raise Exception("Login failed, network issue")
                return True
            except Exception as e:
                raise Exception(f"Login failed {e}")
        if booking_status == "Book Class":
            booking_buttons[info_index[n]].click()
            try:
                booked_count+=1
                booking_buttons[info_index[n]].click()
                time.sleep(2)
                error_elem = driver.find_elements(By.CSS_SELECTOR,'.ClassCard_cardHeader__D9pf3 .ClassCard_errorMessage__Xwjwz')
                if error_elem:
                    raise Exception("Login failed, network issue")
                return True
            except Exception as e:
                raise Exception(f"Login failed {e}")
        if booking_status == "Waitlisted":
            already_booked_waitlisted+=1
        n+=1
    print(f"Booking process done{booked_count,waitlist_count,already_booked_waitlisted}")
    counts = [booked_count,waitlist_count,already_booked_waitlisted]
    return counts
