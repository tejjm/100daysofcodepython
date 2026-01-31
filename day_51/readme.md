# Internet Speed Complaint Bot – Day 51/100DaysOfCode

A Selenium-based bot that:
- Measures your current internet download & upload speeds via Speedtest.net
- If speeds are below your promised values (300 Mbps down / 300 Mbps up in this case), it automatically logs into Bluesky (bsky.app) and posts a complaint tweet-style message tagging your ISP.

**Built while following Angela Yu’s Python course** — great practice for advanced Selenium: undetected driver, explicit waits, human-like typing simulation, and handling dynamic pages.

**Important notes**
- This is a **learning / proof-of-concept project only**.
- Automating posts on social platforms can violate their Terms of Service → use responsibly and never spam.
- Tested with dummy/throwaway credentials — **do not use real accounts for automation** without permission.
- Switched to Bluesky after X login proved tricky (common with modern anti-bot measures).
- Uses `undetected_chromedriver` to reduce detection risk during development.

## What it does
1. Opens Speedtest.net → runs a speed test → extracts download/upload speeds.
2. Compares against promised speeds.
3. If below threshold → navigates to Bluesky → composes a new post with human-like typing delays → publishes complaint.
4. Keeps browser open at end so you can inspect (press Enter to close).

## Tech used
- Python
- `undetected_chromedriver` (bypasses basic bot detection)
- Selenium WebDriver with explicit waits (`WebDriverWait`, `expected_conditions`)
- Random delays for realistic typing
- Chrome profile persistence (optional)

## Requirements
```txt
undetected-chromedriver
selenium  # usually comes with undetected-chromedriver