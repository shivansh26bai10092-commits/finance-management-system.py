# finance-management-system.py
A command-line personal finance manager in Python to track income and expenses, view category reports, and get budget warnings, with data saved locally in JSON. 
# Personal Finance Manager 💰

## 📌 Project Description

The **Personal Finance Manager** is a Python-based command-line application designed to help users manage their personal finances efficiently. It allows users to record income and expenses, track their spending, monitor their monthly budget, and view financial summaries.

The application stores transaction data in a JSON file, ensuring that financial records are preserved even after the program is closed.

## ✨ Features

* **Add Income:** Record income from sources such as salary, pocket money, scholarships, and gifts.
* **Add Expenses:** Track expenses under categories like food, travel, books, shopping, bills, and entertainment.
* **View Transactions:** Display all recorded transactions, sorted by date.
* **Financial Summary:** View total income, total expenses, current balance, and monthly financial details.
* **Category-wise Expense Report:** Analyze spending by category using a simple text-based bar chart.
* **Monthly Budget Management:** Set a monthly spending limit and receive warnings when spending reaches 80% of the budget or exceeds it.
* **Delete Transactions:** Remove unwanted transactions using their unique ID.
* **Persistent Data Storage:** Save and load financial records using a JSON file.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Modules:** `json`, `datetime`
* **Data Storage:** JSON file (`finance_data.json`)
* **Interface:** Command-Line Interface (CLI)

## 🚀 How to Run the Project

### Prerequisites

* Python 3.x installed on your system.

### Steps

1. Download or clone this repository.

2. Open a terminal or command prompt in the project folder.

3. Run the following command:

   ```bash
   python finance_manager.py
   ```

4. Use the numbered menu to select the desired operation.

5. Your financial data will be saved automatically in `finance_data.json`.

## 📂 Project Structure

```text
Personal-Finance-Manager/
│
├── finance_manager.py    # Main Python application
├── finance_data.json     # Stores financial records (created automatically)
└── README.md             # Project documentation
```

## 🎯 Objective

The objective of this project is to develop a simple and practical financial management tool while applying Python programming concepts such as functions, loops, conditional statements, exception handling, file handling, and data structures.

## 🔮 Future Scope

* Add graphical user interface (GUI) support.
* Generate monthly and yearly financial reports.
* Include data visualization using graphs and charts.
* Add transaction search and filtering options.
* Export financial reports to CSV or PDF.

## 👨‍💻 Project Information

**Project Name:** Personal Finance Manager
**Language:** Python
**Project Type:** Command-Line Application
**Developed as:** College Python Project

---

*This project demonstrates how Python can be used to build a simple and effective personal finance management system.*
