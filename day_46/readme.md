# Official Charts → Spotify Time Machine 🎵⏰
Day 46 • #100DaysOfCode Project

A Python script that lets you travel back in time musically:
- Enter any date (YYYY/MM/DD)
- Scrapes the Official Charts UK Top 100 for that exact week
- Searches Spotify and adds every song it finds to a new private playlist named after the date

Relive the charts from your childhood, first crush, or that one random day in 2008!

## Features
- BeautifulSoup web scraping from officialcharts.com
- Spotify API integration with OAuth2
- Automatic private playlist creation
- Handles missing tracks gracefully
- Clean separation across 3 files (`scrapper.py`, `uri.py`, `playlist.py`)

## Tech Stack
- Python
- BeautifulSoup4
- Requests
- Spotipy
- python-dotenv

## Setup
1. Clone the repo
2. `pip install -r requirements.txt`
3. Create a Spotify Developer app → get Client ID, Client Secret
4. Set up your `.env` file:

SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback (or your redirect URI)

5. Run `python playlist.py` and enter your desired date!

## Example Playlist Names
- 2006-08-12 Top 100 from Official Charts
- 1999-03-27 Top 100 from Official Charts

Made with love while learning to code, one day at a time 💙

#100DaysOfCode | #Python | #SpotifyAPI | #WebScraping
