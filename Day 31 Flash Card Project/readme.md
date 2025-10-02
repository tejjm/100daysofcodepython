Kana Flashcard App – Python Project

A dynamic flashcard app to learn Kana characters (Hiragana and Katakana) using Python's Tkinter library. The app automatically flips flashcards after 3 seconds to show the English Romaji, removes known characters from the list to focus on learning unknown ones, and congratulates the user upon completion. Developed as part of my #100DaysOfCode challenge.

Features
Displays Kana characters on flashcards with automatic flip to Romaji after 3 seconds

Removes known characters as user marks them to focus on unfamiliar ones

Persists learning by dynamically updating the practice list

Intuitive user interface with buttons for known/unknown options

Uses JSON and CSV for data handling and conversion

Visually appealing cards with front and back images

How It Works
Loads Kana character data from a CSV, converts to JSON for easy handling.

Randomly picks a character card to display the Kana character.

Automatically flips card after 3 seconds to reveal Romaji transliteration.

If user marks the card as known, it is removed from the practice list.

When all characters are marked known, displays a congratulatory message.

Interface built with Tkinter, with buttons for marking known/unknown flashcards.

Getting Started
Install Python and Tkinter (usually bundled with Python).

Save all files including main.py, All_Kana.json, images folder with required images.

Run the app via terminal or IDE:

text
python main.py
Click right button to mark known and proceed; wrong button to keep practicing.

What I Practiced & Learned
Combining CSV, JSON, and Tkinter for a functional learning app

Using Tkinter's after() method for automatic UI updates and timed flips

Handling dynamic datasets with add/remove operations

Managing GUI layout, buttons, and images for an engaging user experience

File Structure
KanaFlashApp/
├── main.py
├── data/Hiragana_Katakana_Combined.csv
├── images/ (front card, back card, right and wrong button images)
├── All_Kana.json
└── README.md

Part of #100DaysOfCode
Day 31 complete!