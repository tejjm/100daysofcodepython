Anime Quiz App with GUI and API – Project

An updated quiz application that brings console-based quizzes to life with a graphical user interface built using Tkinter. The app fetches real-time trivia questions from the Open Trivia Database API for dynamic quizzes, and employs Object-Oriented Programming principles for clean modularity and ease of future expansion. Developed as part of my #100DaysOfCode challenge.

Features
GUI quiz interface with Tkinter: buttons, canvas, and live score display

Real-time trivia questions fetched from the Open Trivia Database API

Boolean (True/False) question format with instant feedback on answers

Class-based design to separate quiz logic and user interface

Score tracking and end-of-quiz completion screen

How It Works
data.py fetches 10 True/False questions from the Open Trivia DB API.

Questions are converted into Question objects for easy management.

The QuizBrain class manages quiz progression, user answers, and scoring.

QuizInterface class builds the GUI with Tkinter, displays questions, and handles button clicks for True/False.

The interface shows immediate feedback by changing background colors on answer correctness and disables buttons upon quiz completion.

Getting Started
Make sure Python and required modules are installed (tkinter usually bundled, requests for API calls).

Save all provided code files (main.py, ui.py, quiz_brain.py, question_model.py, data.py) with the respective folders/images for buttons.

Run the main script:

text
python main.py
Answer trivia questions through the GUI until the quiz ends.

What I Practiced & Learned
Consuming external APIs to obtain dynamic data

Building modular Python apps with OOP for separation of concerns

Creating responsive GUI interfaces with Tkinter widgets and canvas

Implementing interactive quiz logic and score tracking

Handling encoded HTML characters with html.unescape

File Structure
QuizApp/
├── main.py
├── ui.py
├── quiz_brain.py
├── question_model.py
├── data.py
├── images/ (true.png, false.png)
└── README.md