##SIMPLE CALCULATOR

def calculator():
    try:
        first_number = float(input("Enter first number :"))
        operator= input("Enter operator :") 
        second_number= float(input("Enter second number :"))
    except ValueError:        
        print("invalid")
        return
    if operator == "+":
        total_sum=first_number+second_number
        print(f"{first_number} {operator} {second_number} = {total_sum}")
    elif operator == "-":
         total_subtraction=first_number-second_number
         print(f"{first_number} {operator} {second_number} = {total_subtraction}")
    elif operator == "*":
        total_multiplication=first_number*second_number
        print(f"{first_number} {operator} {second_number} = {total_multiplication}")
    elif operator == "/":
        if second_number == 0:
            print(f"can't divide by 0")
        else:
            total_division=first_number/second_number 
            print(f"{first_number} {operator} {second_number} = {total_division}")    
    else:
        print("invalid operator")            


    
calculator()