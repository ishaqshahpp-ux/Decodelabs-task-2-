# Decodelabs-task-2-
A command-line expense tracker built in Python that records user expenses, validates input, and continuously calculates the total amount spent.
# Python Expense Tracker CLI

A simple command-line Expense Tracker built in Python that allows users to enter expense amounts, validates the input, and keeps a running total of the total money spent.

---

## Project Overview

This project is a beginner-friendly **Expense Tracker Engine** developed in Python.  
It was created to practice user input handling, loops, conditional logic, exception handling, and state management in a command-line application.

The program allows users to:

- enter expense amounts one by one
- keep track of the running total
- prevent invalid or negative entries
- exit the program while showing the final total spent

---

## Features

- Add expenses continuously through user input
- Maintain a running total of all expenses
- Reject negative expense values
- Handle invalid non-numeric input using `try-except`
- Exit the program safely with a final total summary
- Simple and beginner-friendly command-line interface

---

## Technologies Used

- **Python**
- Core concepts used:
  - variables
  - `while` loop
  - `if` statements
  - `try-except`
  - input validation
  - arithmetic accumulation

---

## How It Works

1. The program starts with `total_spent = 0`.
2. It repeatedly asks the user to enter an expense amount.
3. If the user types `exit`, the program ends and shows the final total.
4. If the input is not a valid number, the program displays an error message.
5. If the expense is negative, the program rejects it.
6. If the input is valid, the expense is added to the running total.
7. The updated total is displayed after each valid expense.

---

## Project Structure

```bash
python-expense-tracker-cli/
│
├── expense_tracker.py
├── README.md
└── .gitignore
```

---

## Source Code

```python
# DecodeLabs - Python Project 2: The Expense Tracker

total_spent = 0

print("=== WELCOME TO DECODELABS PROCESSING PHASE ===")
print("Project 2: The Expense Tracker Engine\n")

while True:
    print(f"Current Status -> Total Spent: {total_spent}")
    user_input = input("Enter your expense amount (or type 'exit' to stop): ").strip()
    
    if user_input.lower() == 'exit':
        print(f"\nFinal Closing Statement -> Total Spent: {total_spent}")
        print("Milestone 2 Qualified! Powered by DecodeLabs.")
        break
        
    try:
        expense = int(user_input)
        
        if expense < 0:
            print("Error: Expense amount cannot be negative!")
            continue
            
        total_spent = total_spent + expense
        print(f"Success: {expense} has been added to your tracker.")
        print("-" * 30)
        
    except ValueError:
        print("Invalid Data: Please enter valid numbers only!")
        print("-" * 30)
```

---

## How to Run This Project

### 1) Make sure Python is installed
Install Python 3 on your system.

### 2) Clone the repository
```bash
git clone https://github.com/your-username/python-expense-tracker-cli.git
```

### 3) Open the project folder
```bash
cd python-expense-tracker-cli
```

### 4) Run the program
```bash
python expense_tracker.py
```

---

## Example Output

```bash
=== WELCOME TO DECODELABS PROCESSING PHASE ===
Project 2: The Expense Tracker Engine

Current Status -> Total Spent: 0
Enter your expense amount (or type 'exit' to stop): 500
Success: 500 has been added to your tracker.
------------------------------

Current Status -> Total Spent: 500
Enter your expense amount (or type 'exit' to stop): 250
Success: 250 has been added to your tracker.
------------------------------
```

---

## Project Logic Summary

This project demonstrates a simple but important programming pattern:

- **state preservation** using a variable outside the loop
- **continuous user interaction** with a `while True` loop
- **error handling** using `try-except`
- **input validation** for safe data entry
- **incremental accumulation** of values over time

---

## Future Improvements

This project can be improved further by adding:

- store every expense in a list
- show expense history
- categorize expenses (food, travel, shopping, etc.)
- calculate daily or monthly summaries
- save expenses to a file
- export expense data to CSV
- create a GUI version using Tkinter
- visualize spending with charts

---

## Learning Outcomes

By building this project, I practiced:

- user input handling in Python
- type conversion using `int()`
- error handling with `try-except`
- validation of numeric values
- maintaining state outside a loop
- accumulation logic with variables
- documenting a Python project professionally on GitHub

---

## Author

**Muhammad Hassan Mussana**  
Python programmer  | Web Development Enthusiast | AI engineer 
