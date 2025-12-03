from bs4 import BeautifulSoup
import requests
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text,"html.parser")
tags = list(soup.find_all("h3",class_="title"))
titles = [tag.text for tag in list(soup.find_all("h3",class_="title"))]
correct_ordered = titles[::-1]
print(correct_ordered)
