OpenTrack — Project Documentation

~Introduction

OpenTrack is a Python-based Contributor Management and Issue Tracking System.

It simulates how open-source platforms manage:

- Contributors
- Issues
- Reports and analytics

This project was developed using only basic Python concepts.

---

~System Structure

The program is divided into three main sections:

---

~Section 1 — Project & Contributors

✔ Project Data

Stored using a tuple:

- Project Name
- Version
- Year Started
- Main Language
- Project Lead

✔ Contributors

- Stored as a list of dictionaries
- Each contributor contains:
  - name
  - role
  - language
  - commits
  - country
  - status

✔ Operations Performed

- Sorting contributor names
- Slicing lists
- Updating dictionary values
- Copying data safely

---

~Section 2 — Issue Tracking

✔ Issues

Stored as a list of dictionaries

Each issue contains:

- id
- title
- type
- priority
- reporter
- status

---

✔ Analysis Performed

* List Operations

- Count open issues using loop
- Update priority of first issue
- Slice last two issues

* Set Operations

- Unique reporters
- Technology stack
- Union, intersection, difference

* Dictionary Operations

- Priority count
- Status grouping
- Top reporter detection

---
 
~ Section 3 — File Handling

✔ Folder Creation

- Uses "os" module
- Checks if folder exists before creating

---

✔ Files Generated

project_report.txt

Contains:

- Project details
- Contributor data
- Issue data
- Top reporter

---

issues.csv

Contains:

- Issue data in CSV format

---

✔ File Reading

- "read()" → full content
- "readline()" → first lines
- "readlines()" → list of lines

Also filters:

- Lines containing Critical / High priority

---

~ Bonus Features

- List comprehension for urgent issues
- Appending urgent issues to report file
- Reading last 6 lines for verification

---

~ Input Validation

The system ensures:

- Names contain only letters
- Commits are numeric
- Country names are valid format
- Programming languages are valid text
- Issue fields match expected values

---

~ Execution Flow

1. Program starts and displays banner
2. User enters contributor data
3. User enters issue data
4. System performs analysis
5. Files are created and saved
6. Files are read and verified
7. Final summary is displayed

---

~ Limitations

- No database (data is not persistent after program ends)
- Input validation is basic (no external verification)
- Runs only in terminal (no GUI)

---

~ Future Improvements

- Add database support
- Add graphical interface
- Improve validation using external libraries
- Add search/filter features

---

~~ Conclusion

This project demonstrates how basic Python concepts can be used to simulate a real-world open-source management system.

It is designed to be simple, educational, and easy to understand.

---
