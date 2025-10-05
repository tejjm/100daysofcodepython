ISS Alert Email Notifier – Python Project

A Python program that uses public APIs to monitor the position of the International Space Station (ISS) relative to your location and sends an email notification when the ISS is overhead at night. This encourages timely sky watching. Developed as part of my #100DaysOfCode challenge.

Features
Uses the Open Notify API to fetch real-time ISS position

Queries Sunrise-Sunset API to determine if it's currently night at your location

Checks if ISS is within 5 degrees latitude and longitude of your set coordinates

Sends an email alert when the ISS is close and visible at night

Runs continuously with checks every 60 seconds using a timed loop

Utilizes Python’s SMTPlib for secure email sending via Gmail

How It Works
Defines your location with latitude and longitude.

Fetches ISS real-time coordinates from Open Notify API.

Obtains sunrise and sunset times for your location to determine night time.

If ISS is near your location and it is night, sends an email alert.

The script repeats this check every minute to keep you updated.

Getting Started
Make sure Python is installed with requests module (pip install requests).

Update the script with your real latitude/longitude, email, and app password.

Run the script in a Python environment:

text
python main.py
Keep your device on with internet to receive timely notifications.

What I Practiced & Learned
Working with REST APIs and parsing JSON responses

Implementing periodic tasks with Python loops and time delays

Handling email sending securely with SMTPlib and Gmail SMTP settings

Combining multiple APIs for a smart location/weather-aware application

Basic real-time alerting system design

File Structure
ISSNotifier/
├── main.py
└── README.md