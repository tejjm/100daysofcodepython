Km to Miles Converter GUI – Python Project

A beginner-friendly GUI application built using Python’s Tkinter library that converts distance from kilometers to miles. This project introduces creating windows, labels, buttons, entry fields, and handling button-press events in Tkinter. It also demonstrates working with function arguments like default values, *args, and **kwargs. Developed as part of my #100DaysOfCode challenge.

Features
Simple graphical window with labeled input and output

Entry box for user input (kilometers) initialized with “0”

Button that triggers conversion when clicked

Converts kilometers to miles using a function

Displays converted miles with updated label on GUI

Uses Tkinter’s grid layout manager for organizing widgets

How It Works
Creates a Tkinter window with title and minimum size.

Adds labels for “Kms”, “is equal to”, and “Miles” as text indicators.

Creates an entry widget for user to input kilometers.

Defines Km_to_Miles function to multiply input by 0.6213712 and update the miles label.

Sets a button to call the conversion function when pressed.

Runs the Tkinter main event loop to keep the window active.

Getting Started
Ensure Python and Tkinter module are installed (Tkinter usually bundled with Python).

Save the script as main.py.

Run the program via terminal or IDE:

text
python main.py
Enter kilometer values in the input box and press “Calculate” to see the result in miles.

What I Practiced & Learned
Using Tkinter to create GUI applications

Managing window and widget layout with grid manager

Handling user input via entry widgets

Connecting button events to functions

Understanding function arguments: default, *args, **kwargs

Planning for future projects like a Pomodoro timer

File Structure
KmToMilesGUI/
├── main.py
└── README.md