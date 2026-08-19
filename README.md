📔 Personal Journal Manager

A simple and beginner-friendly Python project that allows users to write, view, search, and delete personal journal entries. 🐍

The project uses Object-Oriented Programming, file handling, dates, and basic user input to create a simple digital journal that stores entries in a text file.

📌 About the Project

Personal Journal Manager is a console-based application where users can manage their journal entries directly from the terminal.

Each journal entry is saved with the date and time when it was created.

The program stores the entries in a local file named:

journal.txt

✨ Features

•	✍️ Add new journal entries

•	📖 View all saved entries

•	🔍 Search entries using keywords

•	🗑️ Delete all journal entries

•	🕒 Automatically records date and time

•	💾 Saves entries permanently in a text file

•	⚠️ Prevents empty journal entries

•	📂 Checks whether the journal file exists

•	🌱 Beginner-friendly implementation

🧠 Python Concepts Used

This project demonstrates several important Python concepts:

•	🏗️ Classes and objects

•	🧩 Methods

•	📁 File handling

•	📖 Reading files

•	✍️ Writing to files

•	➕ Append mode ("a")

•	🔍 Searching text

•	🗑️ File deletion

•	📂 os module

•	🕒 datetime module

•	🔀 Conditional statements

•	🔁 while and for loops

•	🔤 String methods such as lower(), split(), and strftime()

🏗️ Class Used

📔 JournalManager

The JournalManager class handles all journal-related operations.

It contains the following methods:

✍️ add_entry()

Takes a journal entry from the user and saves it to journal.txt along with the current date and time.

Example:

Enter your journal entry: Today I learned Python file handling.



Entry added.

📖 view_entries()

Reads the journal file and displays all saved entries.

If no journal file or entries are available, the program displays an appropriate message.

🔍 search_entry()

Allows the user to search for a specific word or phrase.

The search is case-insensitive, so uppercase and lowercase letters do not affect the search.

Example:

Enter keyword to search: Python



[2026-08-20 10:30:15]

Today I learned Python file handling.

🗑️ delete_entries()

Allows the user to delete all saved journal entries.

The program asks for confirmation before deleting the journal file.

Delete all entries? (yes/no): yes



All entries deleted.

💾 File Handling

The program uses a text file called journal.txt to store journal entries.

Entries are added using append mode, which allows new entries to be added without removing previous ones.

Example stored data:

[2026-08-20 10:30:15]

Today I learned Python.



[2026-08-20 18:45:20]

Worked on my GitHub project.

🛠️ Requirements

🐍 Python 3.x

The project uses Python's built-in:

•	os

•	datetime

No external libraries are required.

▶️ How to Run

1.	Install Python 3 if it is not already installed.

2.	Download or clone this repository.

3.	Open the project folder in a terminal.

4.	Run the Python file:

python journal_manager.py


Or, on some systems:

python3 journal_manager.py

The journal.txt file will be created automatically when the first journal entry is added.

📋 Menu Options

When the program starts, it displays:

1. Add Entry

2. View Entries

3. Search Entry

4. Delete All Entries

5. Exit

✍️ Add Entry

Creates a new journal entry and automatically records its date and time.

📖 View Entries

Displays all previously saved journal entries.

🔍 Search Entry

Searches the journal for a keyword and displays matching entries.

🗑️ Delete All Entries

Deletes the entire journal file after confirmation.

🚪 Exit

Closes the program and displays:

Goodbye!

📂 Project Structure

personal_journal_manager/

│

├──personal_journal_manager.py

└── README.md

💡 journal.txt is created automatically when the first entry is saved.

🎯 Learning Goal

The main goal of this project is to understand how Object-Oriented Programming and file handling can be combined to create a useful Python application.

This project provides practical experience with classes, methods, file operations, modules, date and time handling, searching, and user interaction. 🚀


________________________________________

⭐ If you found this project useful for learning Python, consider giving the repository a star!



