# EXPENCE-TRACKER
A Python command-line application for managing daily expenses. Users can add, view, edit, and delete expenses, calculate total spending, and identify the highest and lowest expenses. Expense data is stored locally in a text file.

# Features

* Add Expenses: Add multiple expenses with a name and amount.
* View Expenses: Display all expenses or view individual expenses by ID.
* Edit Expenses: Update expense names and amounts.
* Delete Expenses: Remove expenses and automatically reassign IDs.
* Calculate Total Spending: Calculate the total of all expenses or selected expenses.
* Find Highest and Lowest Expenses: Identify the most and least expensive items.
* Input Validation: Validate expense names, amounts, menu choices, and expense IDs.
* Data Persistence: Save expenses to a local text file and load them when the application starts.

# Technologies

* Python 3
* Functions and Modules
* Lists and Dictionaries
* File Handling
* Exception Handling
* Input Validation

# Requirements

* Python 3

# Getting Started

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run the application:

python main.py

    If necessary, use python3 main.py instead.

# Data Storage

Expense records are stored in expenses.txt. The application loads saved data at startup and updates the file whenever expenses are added, edited, or deleted.

# Project Structure

Expense-Tracker/
├── main.py
├── function.py
└── expenses.txt

# Learning Objectives

This project demonstrates practical use of Python fundamentals, including data structures, modular programming, file operations, input validation, and exception handling.

# Future Improvements

* Add automated unit tests.
* Improve error handling.
* Introduce expense categories and filtering.
* Support CSV export.
* Develop a graphical user interface (GUI).