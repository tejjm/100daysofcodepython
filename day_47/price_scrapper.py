from bs4 import BeautifulSoup
import requests
def scrape():
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
    url = "https://appbrewery.github.io/instant_pot/"
    try:
        response = requests.get(url=url,headers=header)
    except Exception as e:
        print(e)
    soup = BeautifulSoup(response.text,"html.parser")
    price = soup.find("div",class_="a-section a-spacing-none aok-align-center aok-relative").find("span",class_="aok-offscreen").text
    int_price = float(price.replace("$",""))
    return int_price