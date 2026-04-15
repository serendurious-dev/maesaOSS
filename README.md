OpenTrack — Contributor & Issue Management System
This is a Python-based project I built as part of my Introduction to Open Source Software (Week 5 Assignment).

The goal of this project is to simulate a simple Contributor Management and Issue Tracking System, similar to how real open-source platforms (like GitHub) manage contributors and issues.

---

~Project Overview

In this project, I designed a system that:

- Registers contributors with validation
- Tracks and manages issues
- Performs analysis on contributors and issues
- Saves reports and data into files
- Reads and processes stored data
- Identifies urgent issues automatically

All of this is implemented using basic Python concepts, without using advanced libraries.

---

~Features

🔹 Contributor Management

- Add exactly 4 contributors using user input
- Each contributor includes:
  - Name (validated: no numbers allowed)
  - Role
  - Programming language (validated)
  - Number of commits (must be numeric)
  - Country (validated)
- Automatically assigns Active status
- Stores data using dictionaries and lists

---

~Issue Tracking System

- Add exactly 5 issues with:
  - ID, Title, Type, Priority, Reporter, Status
- Input validation for:
  - Type → Bug / Feature
  - Priority → Critical / High / Medium / Low
  - Status → Open / In Progress / Resolved

---

~Data Analysis

- Count open issues using loops (no shortcuts)
- Update issue priority dynamically
- Extract:
  - Reporters (Set)
  - Tech stack (Set)
- Perform:
  - Union, Intersection, Difference
- Generate:
  - Priority distribution
  - Status-based grouping
- Identify Top Reporter (without using "max()")

---

~File Handling

- Creates project folder automatically
- Saves:
  - 📄 "project_report.txt"
  - 📊 "issues.csv"
- Uses:
  - "os" module
  - "try/except" for safe file operations

---

~File Reading

- Demonstrates:
  - "read()"
  - "readline()"
  - "readlines()"
- Filters lines containing Critical / High priority issues

---

~Bonus Features

- Uses list comprehension to extract urgent issues
- Appends urgent issues to the report file
- Reads and prints last 6 lines to confirm update

---

~Concepts Used

This project covers core Python fundamentals:

- Variables & Data Types
- Tuples, Lists, Dictionaries, Sets
- Loops ("for", "while")
- Conditionals ("if", "elif", "else")
- List Comprehension
- File Handling
- Exception Handling
- String Formatting (f-strings)

---
~How to Run

1. Make sure you have Python 3.10+
2. Run the script:
   python your_file_name.py
3. Follow the input prompts in the terminal

---

~Output Files

After running the program:

- "project_report.txt" → Full project report
- "issues.csv" → Issue data in CSV format

Both files will be created inside a folder named after the project.

---

📌 Notes

- This project is built strictly following assignment rules
- Input validation is added for better reliability
- No advanced libraries were used — only fundamentals

---

