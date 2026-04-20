import pandas as pd
import numpy as np
import os

# Filenames
EXPENSE_FILE = "Expense_History.csv"
CALC_FILE = "History.txt"

def calculator():
    while True:
        try:
            first = float(input("Enter first number :"))
            second = float(input("Enter second number :"))
            op = input("Enter operator (+, -, *, /) :").strip()
            
            # Using a dictionary for cleaner logic instead of many elifs
            operations = {
                "+": first + second,
                "-": first - second,
                "*": first * second,
                "/": first / second if second != 0 else np.nan
            }

            if op not in operations:
                print("Invalid operator.")
                continue
                
            result = operations[op]
            if np.isnan(result):
                print("Error: Division by zero.")
                continue

            output = f"{first} {op} {second} = {result}"
            print(output)

            # Quick save
            with open(CALC_FILE, "a") as f:
                f.write(output + "\n")

            if input("Continue calculating? (y/n): ").lower() != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter numbers.")

def add_expenses():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    
    # Create a small DataFrame for the new entry
    new_data = pd.DataFrame([[amount, category, date]], 
                            columns=["amount", "category", "date"])
    
    # Append to CSV (header=False if file exists, else True)
    file_exists = os.path.isfile(EXPENSE_FILE)
    new_data.to_csv(EXPENSE_FILE, mode='a', index=False, header=not file_exists)
    print("Expense added successfully!")

def analyze_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("No data found.")
        return

    # Load data using Pandas
    df = pd.read_csv(EXPENSE_FILE)
    
    print("\n--- Expense Analysis ---")
    print(f"Total Expenditure: {df['amount'].sum():.2f}")
    
    # Grouping by category (Pandas strength)
    print("\nSpending by Category:")
    print(df.groupby("category")["amount"].sum())

    # Finding the max using NumPy/Pandas logic
    max_idx = df["amount"].idxmax()
    print(f"\nHighest single expense: \n{df.iloc[max_idx]}")

# Main Menu
menu_actions = {
    1: calculator,
    2: add_expenses,
    3: lambda: print(pd.read_csv(EXPENSE_FILE)) if os.path.exists(EXPENSE_FILE) else print("No history."),
    4: analyze_expenses
}

while True:
    print("\n1. Calc | 2. Add Exp | 3. View Exp | 4. Analyze | 5. Exit")
    try:
        choice = int(input("Choose: "))
        if choice == 5: break
        menu_actions.get(choice, lambda: print("Invalid choice"))()
    except Exception as e:
        print(f"An error occurred: {e}")