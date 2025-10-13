Stock Notifier App – Python Project

A Python app that monitors daily stock price changes and sends email alerts if the stock price changes significantly. It integrates the Alpha Vantage stock API with NewsAPI to fetch relevant news articles about the company. The app uses email notification via SMTPlib to keep the user informed about important stock movements and news. Developed as part of my #100DaysOfCode challenge.

Features
Fetches daily stock prices using Alpha Vantage API

Compares closing prices of consecutive days to identify significant increases or decreases

Retrieves top 3 related news articles from NewsAPI for context on price movement

Sends well-formatted email alerts with price changes and news headlines using SMTPlib

Handles API requests and error conditions gracefully

Uses dummy dates to accommodate market closure on weekends

How It Works
Sends API request to Alpha Vantage for stock daily time series data.

Extracts closing prices for the last two days (or specified days).

Calculates percentage change and checks if it exceeds a 3% threshold.

If threshold crossed, fetches top news articles relevant to the company using NewsAPI.

Formats a message including stock change and key news headlines.

Sends an email alert via Gmail SMTP with the compiled message.

Getting Started
Obtain API keys for Alpha Vantage and NewsAPI and replace placeholders in the script.

Ensure Python, requests package, and SMTPlib support are installed.

Save all code files (main.py, news.py) in the same directory.

Run the main script:

text
python main.py
Check email for stock alert notifications when the threshold is crossed.

What I Practiced & Learned
Using multiple APIs in one project and handling their requests and responses

Extracting, processing, and comparing financial data programmatically

Collecting and summarizing news based on API query results

Composing and sending multipart emails with essential information

Managing exceptions and dynamic date handling for financial markets

File Structure
StockNotifier/
├── main.py
├── news.py
└── README.md

