##################### Birthday Wisher ######################
import datetime as dt
import random
import smtplib
import pandas as pd
my_email = "johnbeenrecruiting@gmail.com"
password = "nmky rvtg iqpv nzri"

day = dt.datetime.now().day
month = dt.datetime.now().month
today = (month,day)

df = pd.read_csv("birthdays.csv")
new_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in df.iterrows()}
if today in new_dict:
    path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = new_dict[today]
    with open(path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person.email,
                            msg=f"Subject: Happy Birthday!!\n\n{contents}")


