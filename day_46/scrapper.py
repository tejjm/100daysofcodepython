from bs4 import BeautifulSoup
import requests
def songs_scrapper():
    time = (input("What year would you like to travel to? Enter in format YYYY/MM/DD\n")).replace("/","")
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
    url = "https://www.officialcharts.com/charts/singles-chart/"+time
    try:
        response = requests.get(url=url,headers=header)
    except Exception as e:
        print(e)
    soup = BeautifulSoup(response.text,"html.parser")
    chart_name_data = soup.find_all("a", class_="chart-name")
    artist_names = soup.find_all("a",class_="chart-artist")
    songs = []
    artists = []
    for name in chart_name_data:
        title_span = name.find("span",class_=None)
        if title_span:
            songs.append(title_span.get_text(strip=True))
    for name in artist_names:
        artist_span = name.find("span")
        if artist_span:
            artists.append(artist_span.get_text(strip=True))
    full_names = []
    for n in range (0,len(songs)-1):
        full_names.append(f"{songs[n]} by {artists[n]}")
    return songs,full_names,time

