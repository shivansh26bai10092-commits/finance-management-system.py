"""
Personal Finance Manager - a command-line project

Features: add income/expenses, view all transactions, summary,
category-wise expense report with bar chart, monthly budget warnings,
delete transactions. Data is saved in a JSON file between runs.

Run with:  python finance_manager.py
"""

import json
from datetime import datetime

DATA_FILE = "finance_data.json"
CURRENCY = "Rs."  # change to $, EUR, etc. if you like
INCOME_CATEGORIES = ["Salary", "Pocket Money", "Scholarship", "Gift", "Other"]
EXPENSE_CATEGORIES = ["Food", "Travel", "Books", "Shopping", "Bills", "Entertainment", "Other"]

MENU = """
========== FINANCE MANAGER ==========
 1. Add income
 2. Add expense
 3. View all transactions
 4. Summary
 5. Expense report by category
 6. Set monthly budget
 7. Delete a transaction
 8. Exit
====================================="""


# ---------- File handling ----------
def load_data():
    """Load saved data, or start fresh if the file is missing or broken."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"budget": 0, "transactions": []}


def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError:
        print("Error: could not save data.")


# ---------- Input helpers ----------
def money(amount):
    """Format a number like 'Rs. 1,250.00'."""
    return f"{CURRENCY} {amount:,.2f}"


def get_amount(prompt):
    """Keep asking until the user enters a positive number."""
    while True:
        try:
            amount = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            return round(amount, 2)


def get_date():
    """Ask for a date in YYYY-MM-DD format; Enter means today."""
    while True:
        text = input("Date (YYYY-MM-DD, Enter for today): ").strip()
        if text == "":
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Invalid date. Example: 2026-09-19")


def choose_category(categories):
    """Show a numbered list of categories and return the chosen one."""
    print("Categories:")
    for number, name in enumerate(categories, start=1):
        print(f"  {number}. {name}")
    while True:
        choice = input("Choose category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        print("Invalid choice, try again.")


# ---------- Calculation helpers ----------
def current_month():
    return datetime.now().strftime("%Y-%m")


def total(data, kind, month=None):
    """Sum all 'income' or 'expense' amounts, optionally for one month."""
    result = 0
    for t in data["transactions"]:
        if t["type"] == kind and (month is None or t["date"].startswith(month)):
            result += t["amount"]
    return result


def check_budget(data):
    """Warn the user if this month's spending is near or over the budget."""
    budget = data["budget"]
    if budget <= 0:
        return
    spent = total(data, "expense", current_month())
    percent = spent / budget * 100
    if spent > budget:
        print(f"!! WARNING: You are OVER budget by {money(spent - budget)}!")
    elif percent >= 80:
        print(f"!  Careful: you have used {percent:.0f}% of this month's budget.")


# ---------- Menu features ----------
def add_transaction(data, kind):
    """Add an income or expense entry."""
    categories = INCOME_CATEGORIES if kind == "income" else EXPENSE_CATEGORIES
    print(f"\n--- Add {kind.title()} ---")
    amount = get_amount("Amount: ")
    category = choose_category(categories)
    note = input("Note (optional): ").strip()
    date = get_date()

    # New id = highest existing id + 1
    new_id = max((t["id"] for t in data["transactions"]), default=0) + 1
    data["transactions"].append({
        "id": new_id, "type": kind, "amount": amount,
        "category": category, "note": note, "date": date,
    })
    save_data(data)
    print(f"Saved: {kind} of {money(amount)} under {category}.")
    if kind == "expense":
        check_budget(data)


def view_transactions(data):
    """Print all transactions in a table, newest first."""
    if not data["transactions"]:
        print("\nNo transactions yet.")
        return

    print(f"\n{'ID':<5}{'Date':<12}{'Type':<9}{'Category':<15}{'Amount':>14}  Note")
    print("-" * 70)
    # Sort by date (then id), newest first
    ordered = sorted(data["transactions"], key=lambda t: (t["date"], t["id"]), reverse=True)
    for t in ordered:
        sign = "+" if t["type"] == "income" else "-"
        amount_text = f"{sign}{t['amount']:,.2f}"
        print(f"{t['id']:<5}{t['date']:<12}{t['type']:<9}{t['category']:<15}{amount_text:>14}  {t['note']}")


def show_summary(data):
    """Show overall and current-month totals plus budget status."""
    income = total(data, "income")
    expense = total(data, "expense")
    month = current_month()
    m_income = total(data, "income", month)
    m_expense = total(data, "expense", month)

    print("\n------------- SUMMARY -------------")
    print(f"Total income   : {money(income)}")
    print(f"Total expenses : {money(expense)}")
    print(f"Balance        : {money(income - expense)}")
    print(f"\nThis month ({month}): income {money(m_income)}, expenses {money(m_expense)}")

    if data["budget"] > 0:
        print(f"Monthly budget : {money(data['budget'])} (left: {money(data['budget'] - m_expense)})")
        check_budget(data)
    else:
        print("No monthly budget set (use option 6).")


def category_report(data):
    """Show how much was spent per category, with a simple bar chart."""
    totals = {}
    for t in data["transactions"]:
        if t["type"] == "expense":
            totals[t["category"]] = totals.get(t["category"], 0) + t["amount"]

    if not totals:
        print("\nNo expenses recorded yet.")
        return

    grand_total = sum(totals.values())
    print("\n------- EXPENSES BY CATEGORY -------")
    # Highest spending first
    for category, amount in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        percent = amount / grand_total * 100
        bar = "#" * int(percent / 5)
        print(f"{category:<15}{money(amount):>16}  {percent:5.1f}%  {bar}")
    print(f"{'TOTAL':<15}{money(grand_total):>16}")


def set_budget(data):
    """Set the monthly spending limit."""
    print(f"\nCurrent monthly budget: {money(data['budget'])}")
    data["budget"] = get_amount("Enter new monthly budget: ")
    save_data(data)
    print(f"Budget set to {money(data['budget'])}.")


def delete_transaction(data):
    """Delete a transaction by its ID after confirmation."""
    if not data["transactions"]:
        print("\nNothing to delete.")
        return

    view_transactions(data)
    choice = input("\nEnter the ID to delete (or press Enter to cancel): ").strip()
    if not choice.isdigit():
        print("Cancelled.")
        return

    for t in data["transactions"]:
        if t["id"] == int(choice):
            if input(f"Delete {t['type']} of {money(t['amount'])}? (y/n): ").lower() == "y":
                data["transactions"].remove(t)
                save_data(data)
                print("Transaction deleted.")
            else:
                print("Cancelled.")
            return
    print("No transaction found with that ID.")


# ---------- Main program ----------
def main():
    data = load_data()
    print("Welcome to your Personal Finance Manager!")

    # Map each menu choice to the function that handles it
    actions = {
        "1": lambda: add_transaction(data, "income"),
        "2": lambda: add_transaction(data, "expense"),
        "3": lambda: view_transactions(data),
        "4": lambda: show_summary(data),
        "5": lambda: category_report(data),
        "6": lambda: set_budget(data),
        "7": lambda: delete_transaction(data),
    }

    while True:
        print(MENU)
        try:
            choice = input("Enter your choice (1-8): ").strip()
            if choice == "8":
                break
            if choice in actions:
                actions[choice]()
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")
        except (KeyboardInterrupt, EOFError):
            print()
            break
    print("Goodbye! Your data is saved.")


if __name__ == "__main__":
    main()
