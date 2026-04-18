# SIMPLE CALCULATOR
import pandas as pd

def calculator():
    while True:
        try:
            first = float(input("Enter first number :"))
            second = float(input("Enter second number :"))
        except ValueError:
            print("Please enter valid number")
            continue
        op = input("Enter operator(+,-,*,/) :")
        if len(op) != 1 or op not in "+-*/":
            print("please enter valid operator")
            continue
        if op == "+":
            result = first+second
        elif op == "-":
            result = first-second
        elif op == "*":
            result = first*second
        elif op == "/":
            if second == 0:
                print(f"can't divide by 0")
                continue
            result = first/second
        print(f"{first} {op} {second} = {result}")
        while True:
            history = input(
                "Do you want to save history(yes/no) :").strip().lower()
            if history in ["yes", "y", "no", "n"]:
                break
            print("Invalid input, try again.")
        if history in ["yes", "y"]:
            with open("History.txt", "a") as file:
                file.write(f"{first} {op} {second} = {result}\n")
        while True:
            view_history_choice = input(
                "Do you want to see the history(yes/no):").strip().lower()
            if view_history_choice in ["yes", "y", "no", "n"]:
                break
            print("Invalid input, try again.")
        if view_history_choice in ["yes", "y"]:
            view_history()
        while True:
            delete_choice = input(
                "do you want to delete history(yes/no) :").strip().lower()
            if delete_choice in ["yes", "y", "no", "n"]:
                break
            print("Invalid input, try again.")
        if delete_choice in ["yes", "y"]:
            clear_history()
        while True:
            again = input("do you want to continue (yes/no) :").strip().lower()
            if again in ["yes", "y", "no", "n"]:
                break
            print("Invalid input, try again.")
        if again in ["no", "n"]:
            break


def view_history():
    try:
        with open("History.txt", "r")as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found")


def clear_history():
    Removed = input(
        "Do you really want to delete history(yes/no):").strip().lower()
    if Removed in ["yes", "y"]:
        with open("History.txt", "w") as file:
            file.write("")
        print("File cleared")


def add_expenses():
    while True:
        try:
            amount = float(input("Enter the amount :"))
        except ValueError:
            print("Please enter valid input")
            continue
        category = input("Enter the category :").strip()
        date = input("Enter the date :")

        with open("Expense_History.csv", "a")as file:
            file.write(f"{amount},{category},{date}\n")
        break


def view_expenses():
    while True:
        try:
            View = input(
                "Do you want to view History for your expenditure (yes/no) :").strip().lower()
            if View in ["yes", "y"]:
                with open("Expense_History.csv", "r")as file:
                    for line in file:
                        amount, category, date = line.strip().split(",")
                        print(f"{amount} | {category} | {date}")
                    return
            elif View in ["no", "n"]:
                return
            else:
                print("Invalid")
            continue
        except FileNotFoundError:
            print("File not found")


def Analyze_Expenses():
    df = pd.read_csv("Expense_History.csv")
    Total = df["amount"].sum()
    print(f"Total Expenses: {Total}")
    Category = df.groupby("category")
    print("Expenses by Category:")
    print(Category["amount"].sum())
    print("Highest Expenses")
    Highest = df["amount"].max()
    maximum = df[df["amount"] == Highest]
    print(f"Highest Expenses : {maximum}")

   



while True:
    try:
        print("1. Calculator")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Analyze Expenses")
        print("5. Exit!")

        chose = int(input("choose :"))
        if chose == 1:
            calculator()
        elif chose == 2:
            add_expenses()
        elif chose == 3:
            view_expenses()
        elif chose == 4:
            Analyze_Expenses()
        elif chose == 5:
            break
    except ValueError:
        print("Please enter again")
