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
        history=input("Do you want to save history(yes/no) :").strip().lower()
        if history in ["yes","y"]:
            with open("History.txt","a") as file:
                file.write(f"{first} {op} {second} = {result} \n")
        elif history in ["no","n"]:
            print("the history is not saved")
        again = input("do you want to continue (yes/no) :").strip().lower()
        if again in ["yes", "y"]:
            continue
        elif again in ["no", "n"]:    
            break

def view_history():
    try:
        with open("History.txt","r")as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("File not found")

calculator()
History = input("Do you want to see the history(yes/no):")
if History in ["yes","y"]:
    view_history()
elif History in ["no","n"]:
    print("Thank you ")          

    





