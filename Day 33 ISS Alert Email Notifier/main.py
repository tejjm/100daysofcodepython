from datetime import datetime
import requests
import smtplib
import time
MY_LAT = 20.419930 #Fake lat and long details obviously, add your details if you to use it
MY_LNG = 90.323029
my_email = "johnbeenrecruiting@gmail.com"
password = "nmky rvtg iqpv nzri"
#ISS Response
def close_to_my_location():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])
    print(latitude)
    print(longitude)
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True
    return False

#Sunrise/Sunset Response
def can_see():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }
    sun_response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().time().hour
    if time_now < sunrise_hour or time_now > sunset_hour:
        return True
    return False

#Sending an email if ISS is closeby
def send_email():
    if close_to_my_location() and can_see():
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(from_addr=my_email,to_addrs="testingforjohn1@outlook.com",
                                msg="Subject:Look Up for ISS\n\n"
                                    "Hey John\n"
                                    "The ISS is very close to you and you can probably see it. Go out now!\n\n"
                                    "Thanks,\n"
                                    "Doe")
    else:
        return print("Not close yet")
while True:
    time.sleep(60)
    send_email()
