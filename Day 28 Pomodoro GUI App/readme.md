Pomodoro Timer – Python Project

A productivity timer application built with Python's Tkinter module implementing the Pomodoro Technique. The app cycles through work sessions and breaks, visually displaying the countdown and notifying the user with a beep sound upon transitions. Developed as part of my #100DaysOfCode challenge.

Features
Simple GUI with timer display and three state indicators: Work, Short Break, Long Break

Dynamic countdown timer showing minutes and seconds

Sound notification on session completion (Windows beep)

Start and Reset buttons to control the timer

Tracks and visually indicates completed work sessions with check marks

Implements Python concepts like dynamic typing and event-based callbacks

How It Works
GUI window created using Tkinter with a tomato image inside a canvas.

When “Start” is pressed, the timer cycles through a series of work sessions and breaks using the Pomodoro Technique (25 min work, 5 min short break, 20 min long break).

A countdown function updates the timer display every second.

When timer reaches zero, a beep plays and the next session or break starts automatically.

The reset button stops the timer and clears all progress.

Checkmarks track and display the number of completed work sessions.

Getting Started
Ensure Python and Tkinter are installed (Tkinter usually bundled).

Save the script as main.py and keep tomato.png image in the same directory.

Run the app in a Python environment that supports GUI:

text
python main.py
Use the Start and Reset buttons to control the Pomodoro timer.

What I Practiced & Learned
Building GUIs with Tkinter widgets (Canvas, Buttons, Labels)

Implementing timers and event-driven programming with .after() method

Managing app state and dynamic UI updates

Using Windows sound beep notifications in Python

Applying Pomodoro productivity concepts programmatically

File Structure
PomodoroTimer/
├── main.py
├── tomato.png
└── README.md

Part of #100DaysOfCode
Day 28 complete!