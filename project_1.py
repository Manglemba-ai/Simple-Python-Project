
def add_expense():
   amount=input("Enter the amount :")
   category = input("Enter your category :")
   date = input("Enter the date :")

   with open("D:\coding\python\expenses.txt","a") as file:
      file.write(f"{amount},{category},{date} \n")


def view_expenses():
   try:
      with open("D:\coding\python\expenses.txt","a") as file:
         for line in file:
            amount,category,date =line.strip().split(",")
            print(amount,"|",category,"|",date)
   except FileNotFoundError:
      print("No Expenses Found.")

def total__expense():
   total = 0
   try:
      with open("D:\coding\python\expenses.txt", "r") as file:
         for line in file:
            amount,_, _ =line.strip().split(",")
            total += float(amount)
            print("Total spending :",total)
   except FileNotFoundError:
      print("No expenses found.")
while True:
   print("\n1. Add Expenes")
   print("2. View Expenes")
   print("3. Show Total")
   print("4.Exit")

   choice = input("Choose: ")
   if choice == "1":
      add_expense()
   elif choice == "2":
      view_expenses()
   elif choice == "3":
      total__expense()
   elif choice == "4":
      break
   else:
      print("Invalid choice")
                    

