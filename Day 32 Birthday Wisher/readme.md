Birthday Wisher – Python Project

An automated birthday email wisher built with Python using Pandas for data handling and SMTPlib for sending personalized emails. The app reads birthdays from a CSV file, selects a random birthday message template, personalizes it, and sends it via email on the correct day. Developed as part of my #100DaysOfCode challenge.

Features
Reads birthday data including names, emails, and dates from a CSV

Checks current date to identify whose birthday it is

Selects a random letter template, replaces placeholder with recipient's name

Sends personalized birthday emails using Gmail’s SMTP server

Utilizes secure connection (TLS) and login credentials for email sending

Automates the birthday wishing process with minimal manual work

How It Works
Loads birthday details from birthdays.csv file.

Compares current month and day to each birthday.

If today matches a birthday, picks a random template letter, and customizes it.

Connects to Gmail’s SMTP service securely and sends the customized birthday wish email.

Can be scheduled to run daily for automated greetings.

Getting Started
Ensure you have Python installed and internet connection for SMTP.

Save the script as main.py alongside birthdays.csv and letter templates folder.

Update my_email and password with valid Gmail credentials (consider using app passwords).

Run the script to automatically send birthday wishes on matching dates.

What I Practiced & Learned
Using Pandas to read CSV and iterate rows

Automating personalized email sending with Python SMTPlib

Random selection and string replacement in templates

Scheduling scripts for daily automated tasks

Practical use of date and time modules for real-world apps

File Structure
BirthdayWisher/
├── main.py
├── birthdays.csv
├── letter_templates/ (multiple text files)
└── README.md

Part of #100DaysOfCode
Day 32 complete!

