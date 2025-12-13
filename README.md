Hey! This is my first attempt at a very basic expense tracker using Python and SQLite. Here's a simple  list of instructions to help you initialize your database and get started!

1. Make sure you read the requirements.txt file to make sure that your system is running the roper compatible libraries.

2. once the proper libraries are instaled, run the db.py file to initialize the database. If it works, an output message reading "Database initlalized" should be displayed. 

3. to add expenses to the database, enter the following into your bash terminal: 
python -m expense:tracker.cli add --date [YYYY-MM-DD] --anount [$$.$$] --category "Category_Name" --notes "Note"