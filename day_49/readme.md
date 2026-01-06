# Gym Class Booking Automation – Day 49/100DaysOfCode

A learning project using **Selenium** to automatically log in to a mock gym booking site, book available classes (or join waitlists) on specific days/times, and verify the bookings.

Built while following Angela Yu’s Python course — leveling up Selenium skills with real-world flow: login → navigation → conditional actions → verification.

## What it does
- Logs into the gym website[](https://appbrewery.github.io/gym/)
- Finds all Tuesday & Thursday classes at 6:00 PM
- Books the class if available, joins waitlist if full, skips if already booked/waitlisted
- Switches to "My Bookings" page and verifies the total number of bookings
- Prints a clean summary: booked, waitlisted, already done, and verified count
- Includes a simple retry mechanism for flaky actions

## Tech used
- Python + Selenium WebDriver
- Explicit waits (`WebDriverWait` + `expected_conditions`)
- Custom retry function for robustness
- Chrome profile persistence (optional)

## Project structure
.
├── main.py          → main script: login, book, verify
├── login.py         → handles login with waits & error check
├── booking.py       → finds & books target classes
├── retry_func.py    → simple retry wrapper
└── chrome_profile/  → (created automatically) stores session


## Setup & Run

```bash
# Install dependencies
pip install selenium

# Run the script
python main.py

Note: Uses dummy credentials that work on this test site:
Email: uttejgym@gmail.com
Password: 123123

The site is a public teaching resource by AppBrewery — perfect for practicing automation safely.
Just another daily practice project while balancing a full-time job and consistent learning.
#100DaysOfCode #Python #Selenium #WebAutomation
