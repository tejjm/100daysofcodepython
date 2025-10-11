Rain Alert App – Python Project

A simple yet practical Python project that uses the OpenWeatherMap API to check upcoming weather forecasts and sends an automated email alert if rain is predicted. This app demonstrates the use of API keys, API parameters, email sending with SMTPlib, and conditional logic based on API data response. Developed as part of my #100DaysOfCode challenge.

Features
Uses OpenWeatherMap’s forecast API with secure API key

Checks next few weather timestamps for rain conditions based on weather codes

Sends a personalized email alert if rain is predicted

Demonstrates API authentication and request parameter handling

Utilizes SMTP with Gmail for email notifications

How It Works
Makes a request to OpenWeatherMap’s forecast endpoint with latitude, longitude, and API key.

Parses the JSON weather forecast data for the next 4 intervals.

Checks weather condition IDs to detect if rain or precipitation is expected.

If rain is detected, sends an alert email using Gmail SMTP service.

SMTP connection is secured with TLS and requires valid credentials.

Getting Started
Get a free API key from OpenWeatherMap and replace the appid parameter.

Ensure Python and requests are installed (pip install requests).

Provide valid Gmail credentials to send emails.

Run the app:

text
python main.py
The app will automatically send an umbrella reminder if rain is forecasted.

What I Practiced & Learned
Understanding why API keys are required for accessing web APIs

Making authenticated API requests with query parameters

Parsing JSON data for specific weather conditions

Sending automated email alerts securely with SMTPlib

Implementing practical realtime notifications in Python projects

File Structure
RainAlertApp/
├── main.py
└── README.md

