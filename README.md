# finance-management-system.py
A command-line personal finance manager in Python to track income and expenses, view category reports, and get budget warnings, with data saved locally in JSON. 
# Personal Finance Manager

## Project Description

The Personal Finance Manager is a Python command line application that helps to manage personal finances. The application helps to monitor income, expenses, budget, and financial overview.

The application stores all the data of the user in a JSON file so that the data remains safe even after closing the application.

## Features

- **Income Adding:** The application allows adding up income from different sources such as salary, pocket money, scholarships, and gifts.
- **Expenses Adding:** The application allows the user to add expenses with different categories such as food, travel, books, shopping, bills, entertainment, etc.
- **View All Transactions:** The application displays all the transactions made by the user in a well-formatted manner sorted according to the date of the transaction.
- **Financial Summary:** The application shows the summary of total income, total expenses, total balance, and monthly financial overview.
- **Expense Report:** The user gets an option to check the expense report in the form of a bar chart for better visualization of the expenses done in different categories.
- **Monthly Budget:** The application allows the user to set a monthly budget and notify when the budget is reaching 80% or has crossed the set budget limit.
- **Delete Transaction:** The application has an option to delete any transaction by the unique transaction ID.
- **Data Persistence:** The application persists all the data of the user in a JSON file.

## Technologies Used

- **Programming Language:** Python
- **Modules:** json, datetime
- **Data Persistence:** JSON file (`finance_data.json`)
- **Interface:** Command-Line Interface

## How to Run the Project

### Prerequisites

- The system must have Python 3.x

### Steps

1. Download or clone this repository
2. Open terminal or command prompt in the project directory
3. Type the following command:

```bash
   python finance_manager.py
```

4. Use the numbered options to choose from the available options
5. The data will be stored in a JSON file for persistence between runs.

## Project Structure

```
Personal-Finance-Manager/
├── finance_manager.py   # Main python application
├── finance_data.json    # Storing data (automatically generated)
└── README.md            # Project documentation
```

The objective of this project is to demonstrate the knowledge of functions, loops, conditions, exceptions, file handling, and data structures in Python by developing a Personal Finance Manager application. The project also aims to provide experience in developing a real-world command-line application.

## Future Scope

The following future scope is planned to be implemented in the near future:

- A GUI (Graphical user interface) should be added to the application.
- The application should generate a monthly report and a yearly report.
- The application should support visualization of financial data using graphs and charts.
- The application should support searching and filtering of transactions.
- The application will allow exporting of reports in CSV or PDF format.

## Project Information

- **Project Name:** Personal Finance Manager
- **Language:** Python
- **Project Type:** Command Line Application
- **Developed as:** College Python Project

The Personal Finance Manager project demonstrates how Python can be used to develop a personal finance management system.
