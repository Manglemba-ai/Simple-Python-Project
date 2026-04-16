
def add_expences():
   amount=input("Enter the amount :")
   category = input("Enter your category :")
   date = input("Enter the date :")

   with open("expences.txt","a") as file:
      file.write(f"{amount},{category},{date} \n")


def view_expences():
   try:
      with open("expences.txt","a") as file:
         for line in file:
            amount,category,date =line.strip().split(",")
            print(amount,"|",category,"|",date)
   except FileNotFoundError:
      print("No Expences Found.")

def total__expences():
   total = 0
   try:
      with open("expences.txt", "r") as file:
         for line in file:
            amount,_, _ =line.strip().split(",")
            total += float(amount)
            print("Total spending :",total)
   except FileNotFoundError:
      print("No expenses found.")
               
