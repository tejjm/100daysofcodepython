USA States Guessing Game – Python Project
A fun and educational game built using Python’s Turtle and Pandas libraries. Players guess the names of the 50 US states on a blank map. Correct guesses get marked on the map; players can exit anytime to save a list of missed states for further learning. Developed as part of my #100DaysOfCode challenge.

Features
Displays a blank US map using Turtle graphics

Prompts players to guess state names with unlimited tries

When a correct guess is made, the state name is displayed at the correct coordinates on the map

Player can type "Exit" anytime to end the game

Saves a CSV file containing all states not guessed for study

How It Works
Loads a blank US map image as the Turtle background.

Reads the 50 states and their coordinates from a CSV file using Pandas.

Uses a text input prompt repeatedly to get guesses from the player.

Validates guesses against the states list, then writes the names directly onto the map.

Tracks correct guesses and calculates missed states for CSV export upon exit.

Getting Started
Ensure Python’s Turtle and Pandas modules are installed (pip install pandas).

Save all files (main.py, writer.py, 50_states.csv, blank_states_img.gif) in the same directory.

Run the game in a Python environment that supports GUI:

text
python main.py
Enter the names of US states when prompted, or type "Exit" to quit.

Check the generated missed_states.csv for states to study.

What I Practiced & Learned
Combining Turtle graphics with data handling using Pandas

Managing user input and validating against a data source

Displaying text dynamically on a graphical map

File handling and exporting data to CSV

Real-time game feedback and interactive GUI prompts

File Structure
USAStatesGame/
├── main.py
├── writer.py
├── 50_states.csv
├── blank_states_img.gif
├── missed_states.csv (generated upon exit)
└── README.md

Part of #100DaysOfCode
Day 25 complete!

Day 25 of #100DaysOfCode 🇺🇸🐢
Built a USA States Guessing game combining Turtle and Pandas!

Guess the states on a blank map with unlimited tries

Correct guesses labeled on the map in real-time

Missed states saved to CSV for learning after exiting
Fun and educational project deepening Python GUI + data handling skills! 🎯

#Python #CodingJourney

(Video and flow chart below)# USA States Guessing Game – Python Project

A fun and educational game built using Python’s Turtle and Pandas libraries. Players guess the names of the 50 US states on a blank map. Correct guesses get marked on the map; players can exit anytime to save a list of missed states for further learning. Developed as part of my #100DaysOfCode challenge.

Features
Displays a blank US map using Turtle graphics

Prompts players to guess state names with unlimited tries

When a correct guess is made, the state name is displayed at the correct coordinates on the map

Player can type "Exit" anytime to end the game

Saves a CSV file containing all states not guessed for study

How It Works
Loads a blank US map image as the Turtle background.

Reads the 50 states and their coordinates from a CSV file using Pandas.

Uses a text input prompt repeatedly to get guesses from the player.

Validates guesses against the states list, then writes the names directly onto the map.

Tracks correct guesses and calculates missed states for CSV export upon exit.

Getting Started
Ensure Python’s Turtle and Pandas modules are installed (pip install pandas).

Save all files (main.py, writer.py, 50_states.csv, blank_states_img.gif) in the same directory.

Run the game in a Python environment that supports GUI:

text
python main.py
Enter the names of US states when prompted, or type "Exit" to quit.

Check the generated missed_states.csv for states to study.

What I Practiced & Learned
Combining Turtle graphics with data handling using Pandas

Managing user input and validating against a data source

Displaying text dynamically on a graphical map

File handling and exporting data to CSV

Real-time game feedback and interactive GUI prompts

File Structure
USAStatesGame/
├── main.py
├── writer.py
├── 50_states.csv
├── blank_states_img.gif
├── missed_states.csv (generated upon exit)
└── readme.txt