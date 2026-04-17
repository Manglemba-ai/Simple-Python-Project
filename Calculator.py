# SIMPLE CALCULATOR

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
            if again in ["yes", "y","no", "n"]:
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


calculator()
