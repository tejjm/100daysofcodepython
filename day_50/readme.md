# Tinder Automation Bot – Day 50/100DaysOfCode (Educational Only)

**Purely a learning project** to explore advanced browser automation with Selenium.  
**This bot was tested on a throwaway account that has now been permanently deleted.**  
**I will not use or run this on any real/personal accounts.**

Built as part of Angela Yu’s Python course to practice:
- Handling login flows
- Interacting with dynamic web elements
- Randomizing actions to mimic human behavior
- Dealing with pop-ups, waits, and potential CAPTCHAs

**Important Disclaimers**
- Automating Tinder (or any dating app) **violates Tinder's Terms of Service** and can result in permanent account bans or IP blocks.
- This project is **for educational purposes only** — understanding web automation, not for actual use on live dating platforms.
- Tinder actively detects and bans automated behavior (swipe patterns, timing, etc.).
- Respect user privacy and consent — never use automation to interact with real people without genuine intent.
- No data was scraped or stored; the script was run briefly for proof-of-concept.

## What it does (high-level)
- Opens Tinder web in Chrome
- Automates login (manual intervention possible for 2FA/phone)
- Swipes (left/right) on profiles with randomized delays
- Handles basic pop-ups/modals

## Tech used
- Python
- Selenium WebDriver (Chrome)
- Explicit waits & exception handling
- Random sleep intervals for human-like behavior

## Setup & Run (for learning only)

```bash
# Install dependencies
pip install selenium

# (Optional) Use webdriver-manager for auto ChromeDriver
pip install webdriver-manager

# Run the script
python tinder_bot.py
