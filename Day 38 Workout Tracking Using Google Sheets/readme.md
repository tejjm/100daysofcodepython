Workout Tracker with Nutritionix & Sheety APIs – Python Project

A Python app to log workout activities using natural language input. The app utilizes the Nutritionix API to parse exercise details and calculate calories burned, and the Sheety API to record the data in a Google Sheets spreadsheet in real-time. This project demonstrates integration of multiple APIs, secure handling of authentication credentials, and automation for fitness tracking. Developed as part of my #100DaysOfCode challenge.

Features
Takes natural language input for exercises (e.g., "ran 30 minutes and did 20 pushups")

Uses Nutritionix API to retrieve detailed workout data including calories and duration

Sends workout data to Google Sheets via Sheety API for organized logging

Manages API keys and tokens securely through environment variables

Prints response status to verify successful logging

How It Works
Accepts user input describing workout details in plain language.

Sends request to Nutritionix API with personal stats for accurate calculation.

Parses returned exercise data for each activity performed.

Posts each exercise entry to Google Sheets using Sheety API and bearer token.

Displays status code and response for each API call to ensure logging success.

Getting Started
Obtain API keys for Nutritionix and Sheety and set environment variables (N_API_ID, N_API_KEY, BEARER_AUTH).

Install Python requests library:

text
pip install requests
Save script and run:

text
python main.py
Follow prompts to enter exercise details.

What I Practiced & Learned
Working with multiple external APIs simultaneously

Processing JSON responses and handling nested data

Securely managing API credentials with environment variables

Automating data logging to Google Sheets

Enhancing user interaction via natural language processing API

File Structure
WorkoutTracker/
├── main.py
└── README.md