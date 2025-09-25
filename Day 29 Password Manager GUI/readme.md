Password Manager GUI – Python Project

A secure and user-friendly password manager built using Python's Tkinter library. The app generates random strong passwords, copies them to the clipboard for easy pasting, and saves website, email, and password combinations in a local text file. Developed as part of my #100DaysOfCode challenge.

Features
Generates random passwords mixing letters, numbers, and symbols

Copies generated passwords directly to clipboard using pyperclip

Saves password entries (website, email/username, password) to a local text file

Uses Tkinter for a clean and intuitive graphical user interface

Includes input validation and confirmation dialogs to prevent empty or incorrect entries

How It Works
User inputs website name and email/username.

Clicking "Generate Password" creates a strong random password which is displayed and copied to clipboard automatically.

Clicking "Add" saves all the details in a file (passwords.txt) with confirmation prompt.

Fields reset after saving for new entries.

Getting Started
Ensure Python, Tkinter, and pyperclip module are installed (pip install pyperclip).

Save the script as main.py alongside the image file logo.png.

Run the app in a Python environment that supports GUI:

text
python main.py
Use the interface to generate and store passwords securely.

What I Practiced & Learned
Building interactive GUI apps with Tkinter widgets

Generating random secure passwords with lists and the random module

Using clipboard integration with Python’s pyperclip module

Validating user input and showing confirmation dialogs

Writing data to local files responsibly

File Structure
PasswordManagerGUI/
├── main.py
├── logo.png
├── passwords.txt (created on first save)
└── README.md

Part of #100DaysOfCode
Day 29 complete!
