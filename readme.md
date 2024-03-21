# Academy model

### Description
This app is based on PyQt5 library, but the main focus is to demonstrate many-to-many relationship using SQLite database.

In modules folder 'db.py' create a database using 3 tables: student, advisor and advisor-student. The latter is responsible for storing the
above-mentioned relationship between advisors and students.

'personnel.py' has student and advisor classes for creating, searching and similar database operations.

'guy.py' is responsible for actual app functionality.

Run 'main.py' to use the application.

### Requirements
- Python 3.9
- PyQt5

to install required packages run in terminal:
- pip install -r requirements.txt

### How to use app
The first page allows user to enter new student's name and surname and choose at least one advisor for that student.
click 'Save' button to add the new student and their advisors to database tables.

'Search student' button will switch page and user will be able to choose an advisor from dropdown list to search all students that advisor has.

Enjoy and share your thoughts!
