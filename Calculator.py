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
        again = input("do you want to continue (yes/no) :").strip().lower()
        if again in ["yes", "y"]:
            continue
        elif again in ["no", "n"]:
            print("Thank you")
            break


calculator()
