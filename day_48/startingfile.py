from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint
URL = "https://www.python.org/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
# price = driver.find_element(By.XPATH,value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]').text
# print(f"The shirts price today is {price}")
# event_times = driver.find_elements(By.CSS_SELECTOR,"div.medium-widget.event-widget.last ul.menu li time")
# events = driver.find_elements(By.CSS_SELECTOR,"div.medium-widget.event-widget.last ul.menu li a")
events = driver.find_elements(By.CSS_SELECTOR,"div.medium-widget.event-widget.last ul.menu li")
# for event in event_times:
#     print(event.text)
# time = [time.text for time in event_times]
# events = [event.text for event in events]
event_details = {}
event_list = []
for event in events:
    split =event.text.split("\n")
    event_details["time"] = split[0]
    event_details["name"] = split[1]
    event_list.append(event_details)
pprint(event_list)
driver.quit()