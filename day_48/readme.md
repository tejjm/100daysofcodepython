# Cookie Clicker Automation – Day 48/100DaysOfCode

A fun learning project using **Selenium** to automate the classic Cookie Clicker game and maximize cookies per second (CPS) in a fixed time.

Goal: Click the big cookie non-stop while intelligently buying the most expensive upgrades I can afford every 5 seconds — all automated!

Built as part of Angela Yu’s Python course. First time diving into browser automation with Selenium.

## What it does
- Opens Cookie Clicker in Chrome
- Selects English language
- Clicks the big cookie repeatedly for 5-second bursts
- Every 5 seconds: checks current cookie count and buys as many of the highest-available upgrades as possible (prioritizing most expensive first)
- Runs for 3 minutes (180 seconds)
- Prints final Cookies per Second (CPS) score

## Tech used
- Python
- Selenium WebDriver (Chrome)
- Basic time & regex for parsing

## Requirements
- Google Chrome browser installed
- ChromeDriver (managed automatically if you have `webdriver-manager` — see setup)

## Setup & Run

```bash
# 1. Install dependencies
pip install selenium webdriver-manager

# 2. Save the script as cookie_clicker_bot.py (or any name)

# 3. Run it
python cookie_clicker_bot.py

Game URL
https://ozh.github.io/cookieclicker/
Just a daily practice project while balancing a full-time job and consistent learning.
#100DaysOfCode #Python #Selenium #Automation


