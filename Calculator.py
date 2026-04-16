# SIMPLE CALCULATOR

def calculator():
    try:
        first = float(input("Enter first number :"))
        second = float(input("Enter second number :"))
    except ValueError:
        print("Please enter valid number")
        return
    op = input("Enter operator(+,-,*,/) :")
    if len(op) != 1 or op  not in "+-*/":
        print("please enter valid operator")
        return
    if op == "+":
        result = first+second
    elif op == "-":
        result = first-second
    elif op == "*":
        result = first*second
    elif op == "/":
        if second == 0:
            print(f"can't divide by 0")
            return
        result = first/second
    print(f"{first} {op} {second} = {result}")


calculator()
