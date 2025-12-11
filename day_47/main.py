from price_scrapper import scrape
from mail import send_mail
price=scrape()
message = f"Hey the price for your item is reduced to ${price}"
if price < 100:
    send_mail(message=message)