from bs4 import BeautifulSoup
import requests
time = input("What year would you like to travel to? Enter in format YYYY-MM-DD\n")
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
print(type(time))
