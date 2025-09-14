NATO Phonetic Alphabet Converter – Python Project

A simple yet powerful Python program that converts any input word into its corresponding NATO phonetic alphabet codes. Built using Pandas to read a CSV file, and leveraging dictionary and list comprehensions for efficient data handling. Developed as part of my #100DaysOfCode challenge.

Features
Reads NATO phonetic alphabet data from a CSV file

Creates a dictionary mapping each letter to its phonetic code using dictionary comprehension

Takes user input and converts each letter to its phonetic equivalent using list comprehension

Handles user input case-insensitively, converting input to uppercase for matching

Outputs a list of phonetic code words corresponding to the input word

How It Works
Loads nato_phonetic_alphabet.csv containing letters and code words using Pandas.

Creates a dictionary mapping letters to phonetic codes using df.iterrows().

Asks the user to input a word.

Converts each letter in the input to its corresponding phonetic code if it exists in the dictionary.

Prints the list of phonetic codes for the user’s input word.

Getting Started
Ensure Python and Pandas are installed (pip install pandas).

Save main.py and nato_phonetic_alphabet.csv in the same directory.

Run the program with:

text
python main.py
Enter any word when prompted to get its NATO phonetic equivalent.

What I Practiced & Learned
Reading CSV files into DataFrames using Pandas

Efficient dictionary creation with dictionary comprehension

List comprehension combined with conditional checks

Handling user input and string manipulation

Connecting data processing with user interaction

File Structure
NATOPhoneticConverter/
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md

Part of #100DaysOfCode
Day 26 complete!
