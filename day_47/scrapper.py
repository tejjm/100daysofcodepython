from bs4 import BeautifulSoup
import requests
def scrape():

    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36","ACCEPT-LANGUAGE":"en-US,en;q=0.9"}
    url = "https://www.amazon.in/Sony-Playstation-Dualsense-Controller-White/dp/B08KJPLGLF/ref=sr_1_3?crid=29GD59F1A0TLW&dib=eyJ2IjoiMSJ9.zV21GBvuwdpHNt522meN5fhovVB5H06iJ_yrEcl7ON6-LNIRHAnKaXX9lXpLCkeKEeq8lZL6i9aUcY8HenRiBBS-B2NSJzgOUIw3oSaibU2lovnvdthMV3x-rOw4VvHZl67kq_szFF1DtUKpS3tWhwIh9RlTHaOXYXgLV40IJCCbU_sg5PbkktyosHAxe4xYQl478smrSTGPcP5_zuRTztUIfQM_pTZ2N-KvMDWWh5E.ZrEptZvjjC5HPDoho9aeicajXQkM8h3N5h5ed6pwUpE&dib_tag=se&keywords=ps+5+controller&qid=1765469059&sprefix=ps+5+controlle%2Caps%2C193&sr=8-3"
    try:
        response = requests.get(url=url,headers=header)
    except Exception as e:
        print(e)
    soup = BeautifulSoup(response.text,"html.parser")
    price = soup.find("div",class_="a-section a-spacing-none aok-align-center aok-relative").find("span",class_="a-price-whole").text
    int_price = float(price.replace(",",""))
    product = (soup.find("div",id="titleSection").find("span",id="productTitle").text).strip()
    return int_price,product