import requests
import smtplib
my_email = "johnbeenrecruiting@gmail.com"
password = "nmky rvtg iqpv nzri"
parameters = {
    "appid" : "10a253a0e260c91078fb532965afa897",
    "lat" : 38.255508,
    "lon" : 140.336334,
    "cnt" : 4
}
end_point = "https://api.openweathermap.org/data/2.5/forecast??"
response = requests.get(end_point,params=parameters)
response.raise_for_status()
data = response.json()["list"] #[0]["weather"][0]["id"]
will_rain = False
def send_alert():
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="testingforjohn1@outlook.com",
                            msg="Subject: It's going to rain!\n\n"
                                "Hey Homie it's going to rain today, Take your umbrella with you!\n\n"
                                "Your's Truly,\n"
                                "Rainbot")
for n in range(0,4):
    if data[n]["weather"][0]["id"] < 700:
        will_rain = True
    else:
        will_rain = False
if will_rain:
    send_alert()


