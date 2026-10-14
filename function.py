expenses = []
def add_expense():
    # Get a valid expense count
    while True:
        try:
            expense_count = int(input("How many Expenses do you want to add? : "))
            if expense_count > 0:
                break
            else:
                print("please enter the number")
        except ValueError:
            print("please enter the number")
    #Add each expense
    for i in range(expense_count):
         print(f"\nAdding expense {i + 1} of {expense_count}")
         #Get a valid name
         while True:
                expense_name = input("please enter the expense name:").strip().title()
                if expense_name and not expense_name.isdigit():
                    break
                else:
                    print("please enter the name")
         #Get a valid amount
         while True:
                try:
                    expense_amount = float(input("please enter the expense amount: "))
                    if expense_amount > 0:
                            break
                    else:
                            print("amount must be greater than zero")
                except ValueError:
                        print("please enter the number")
         #Creat one expense
         expense = {
                    "id": len(expenses) + 1,
                    "name": expense_name,
                    "amount": expense_amount
                }
         #Add it to the list
         expenses.append(expense)
         get_expenses()
         print("Expense added successfully")

    print(expenses)

def get_expenses():
    with open ("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense["id"]},{expense['name']},{expense['amount']}\n")

def load_expenses():
    expenses.clear()
    try:
       with open ("expenses.txt", "r") as file:
          for line in file :
              expense_id , expense_name , expense_amount = line.strip().split(",")
              expense={
                  "id": int(expense_id),
                  "name": expense_name,
                  "amount": float(expense_amount)
               }
              expenses.append(expense)
    except FileNotFoundError:
        pass