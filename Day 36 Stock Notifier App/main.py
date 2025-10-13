import requests
from email.mime.text import MIMEText
from datetime import date,timedelta
import smtplib
import news
my_email = "johnbeenrecruiting@gmail.com"
password = "nmky rvtg iqpv nzri"
STOCK = "TSLA"
STOCK_API = "JOZ6GQV7Q71K1KMR"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : STOCK_API
}
today = date.today()
today_formated = today.strftime("%Y-%m-%d")
yesterday = "2025-10-10"#(today - timedelta(days=2)).strftime("%Y-%m-%d")
day_before_yesterday = "2025-10-09"#(today - timedelta(days=3)).strftime("%Y-%m-%d")
stock_response =requests.get(STOCK_ENDPOINT,params=stock_params)
stock_response.raise_for_status()
print(stock_response.json())
#Getting the closing price information for last two consecutive days
condition = False
# if today.weekday() > 4:
#     condition = True
#Changed above for testing
if condition:
    print("Market is closed, Notification will be sent of Tuesday")
else:
    yesterday_closing = float(stock_response.json()["Time Series (Daily)"][yesterday]["4. close"])
    daybefore_yest_closing = float(stock_response.json()["Time Series (Daily)"][day_before_yesterday]["4. close"])
    if yesterday_closing < daybefore_yest_closing:
        reduced_by = round(((daybefore_yest_closing - yesterday_closing) / daybefore_yest_closing) * 100, 2)
        reduced_msg = f"{STOCK} reduced by: {reduced_by}%"
        print(f"Reduced by {reduced_by}%")
    else:
        increased_by = round(((yesterday_closing - daybefore_yest_closing) / today_formated) * 100, 2)
        increased_msg = f"{STOCK} increased by: {increased_by}%"
        print(f"Increased by {increased_by}%")
if reduced_by or increased_by > 3:
    if reduced_by is None:
        msg = increased_msg
    else:
        msg = reduced_msg
    details = news.get_news()
    msg_body = (
        f"{msg}\n"
        f"{details[0]}\n"
        f"{details[1]}\n"
        f"{details[2]}\n\n"
        "Yours truly,\nTrady"
    )

    # Creating a MIMEText object with UTF-8 encoding
    mime_msg = MIMEText(msg_body, _charset='utf-8')
    mime_msg['Subject'] = "Hey here's your stock details"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs="testingforjohn1@outlook.com",
                            msg=mime_msg.as_string())

