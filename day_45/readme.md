Top 100 Movies Scraper – Python Project
A web scraper built with BeautifulSoup and Requests that extracts the top 100 movies from Empire Online's list, reorders them correctly, and saves to a text file. Developed as part of my #100DaysOfCode challenge.​

Features
Fetches HTML from archived Empire Online best movies page

Targets <h3 class="title"> elements using CSS selectors

Extracts movie titles via list comprehension

Reverses list to match correct ranking order

Writes ordered titles to "Top 100 Movies.txt"

Combines HTML/CSS knowledge with Python file handling

How It Works
Sends GET request to archived Empire Online top movies page using Requests.
Parses HTML with BeautifulSoup and finds all h3.title tags containing movie names.
Uses list comprehension to extract text, reverses order with slicing [::-1] for correct ranking.
Opens file in write mode and loops through titles, writing each to a new line.

Getting Started
Install required packages:

text
pip install requests beautifulsoup4
Save the script as main.py.
Run in your terminal:

text
python main.py
Outputs printed list + creates "Top 100 Movies.txt" with ranked titles.

What I Practiced & Learned
Web scraping with Requests + BeautifulSoup(html.parser)

CSS class selectors (class_="title") from HTML/CSS knowledge

List comprehensions for efficient data extraction

File creation/writing with context managers (with open)

String slicing [::-1] for list reversal

File Structure
text
MoviesScraper/
├── main.py
└── README.md
└── Top 100 Movies.txt (generated)
Part of #100DaysOfCode
Day 45 complete!
