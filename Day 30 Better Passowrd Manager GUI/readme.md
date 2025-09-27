Password Manager with JSON and Search – Python Project

An enhanced password manager GUI app built with Python’s Tkinter and JSON modules. This version improves file handling by saving credentials in a human-readable JSON format. Added a powerful search function to quickly retrieve login details, and implemented exception handling for smooth user experience. Developed as part of my #100DaysOfCode challenge.

Features
Generates strong random passwords with letters, numbers, and symbols

Copies generated passwords automatically to clipboard

Saves website, email, and password combos in a structured JSON file (passwords.json)

Search functionality to fetch and display saved credentials by website

Handles missing files and non-existent website queries gracefully with error dialogs

User-friendly GUI built with Tkinter featuring input validation and message boxes

How It Works
User inputs website, email/username, and can generate a secure password.

Password data is saved in a JSON file, updating existing entries or creating new ones.

The search button retrieves saved email and password details for a given website.

Exception handling ensures smooth operation when data is missing or incorrect.

Passwords copied to clipboard for instant use.

Getting Started
Install Python and required modules:

text
pip install pyperclip
Save main.py and logo.png in the same directory.

Run the program in a Python environment with GUI support:

text
python main.py
Use the interface to generate, save, and search passwords.

What I Practiced & Learned
Advanced file handling with JSON for structured data storage

Exception handling to improve robustness

Building user-friendly GUI with Tkinter widgets and message boxes

Clipboard integration with pyperclip

Managing state and updates in real-time apps

File Structure
PasswordManagerJSON/
├── main.py
├── logo.png
├── passwords.json (created on use)
└── README.md

Part of #100DaysOfCode
Day 30 complete!