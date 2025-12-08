from bs4 import BeautifulSoup
import requests
time = (input("What year would you like to travel to? Enter in format YYYY/MM/DD\n")).replace("/","")
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
url = "https://www.officialcharts.com/charts/singles-chart/"+time
try:
    response = requests.get(url=url,headers=header)
except Exception as e:
    print(e)
soup = BeautifulSoup(response.text,"html.parser")
chart_name_data = soup.find_all("a", class_="chart-name")
author_names = soup.find_all("a",class_="chart-artist")
clean_names = []
authors = []
for name in chart_name_data:
    title_span = name.find("span",class_=None)
    author_span = name.find("span",class_=None)
    if title_span and author_span:
        clean_names.append(title_span.get_text(strip=True))
        authors.append(author_span.get_text(strip=True))
print(clean_names)
print(authors)
# full_list = []
# for n in len(clean_names):
#     full_list.append(f"{clean_names(n)} by {authors(n)}")
# print(full_list)
# print(len(full_list))
