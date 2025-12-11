from scrapper import scrape
from mail import send_mail
price,product=scrape()
message = f"Hey the price for {product} on your wishlist is reduced to INR{price}"
if price < 7000:
    send_mail(message=message)