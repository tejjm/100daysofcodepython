Habit Tracker with Pixe.la API – Python Project

A habit tracking application that uses the Pixe.la API to record and visualize daily progress with pixel graphs. This project deepened understanding of API methods like POST, PUT, and DELETE, and how to work with dates and JSON data. Developed as part of my #100DaysOfCode challenge.

Features
Creates and manages habit-tracking graphs on Pixe.la via API requests

Posts daily progress data to the graph for visualization

Updates and deletes data points dynamically with PUT and DELETE requests

Manages API authentication securely with tokens

Automates habit recording with date formatting and API interaction

How It Works
Uses requests to send POST requests to create and update user graphs on Pixe.la.

Posts daily quantity of habit performed identified by the current date.

Enables updating of existing data points to correct or extend records.

Deletes data points as needed for habit tracking accuracy.

Logs server responses for confirmation of successful API interaction.

Getting Started
Register on Pixe.la to get your user token and username.

Update script with your token, username, graph ID, and dates as needed.

Run the program to create graphs and post habit data.

What I Practiced & Learned
Using API calls post(), put(), and delete() effectively in Python

Managing HTTP headers and JSON payloads for API interactions

Formatting dates and automating daily habit tracking

Handling online APIs for data visualization and habit monitoring

File Structure
HabitTrackerPixela/
├── main.py
└── README.md