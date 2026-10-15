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
    # Add each expense
    for i in range(expense_count):
        print(f"\nAdding expense {i + 1} of {expense_count}")
        # Get a valid name
        while True:
            expense_name = input("please enter the expense name:").strip().title()
            if expense_name and not expense_name.isdigit():
                break
            else:
                print("please enter the name")
        # Get a valid amount
        while True:
            try:
                expense_amount = float(input("please enter the expense amount: "))
                if expense_amount > 0:
                    break
                else:
                    print("amount must be greater than zero")
            except ValueError:
                print("please enter the number")
        # Creat one expense
        expense = {
            "id": max((item["id"] for item in expenses), default=0) + 1,
            "name": expense_name,
            "amount": expense_amount
        }
        # Add it to the list
        expenses.append(expense)
        save_expenses()
        print("Expense added successfully")

    show_all_expenses()

#---------------------------------------------------------------------------------------

def save_expenses():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense["id"]},{expense['name']},{expense['amount']}\n")

#---------------------------------------------------------------------------------------
def load_expenses():
    expenses.clear()
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",", 2)
                if len(parts) != 3:
                    print(f"invalid expense record : {line}")
                    continue
                try:
                    expense_id = int(parts[0])
                    expense_name = parts[1]
                    expense_amount = float(parts[2])
                except ValueError:
                    print(f"Invalid expense record: {line}")
                    continue

                expenses.append({
                    "id": expense_id,
                    "name": expense_name,
                    "amount": expense_amount
                })

    except FileNotFoundError:
        print("expenses.txt file not found")

#---------------------------------------------------------------------------------------
def edit_expense():
        #select an expense
        expense = select_expense()
        #show the selected expense
        show_expense(expense)
        #Allow repeated edits
        while True:
            choice = input("What do you want to edit ?\n"
                           "1-Edit Name\n"
                           "2-Edit Amount\n"
                           "3-Choose another expense ID\n"
                           "4_Finish editing\n"
                           "PLEASE CHOOSE 1 OR 2 OR 3)\n").strip()
            if choice == "1":
                while True:
                    new_name = input("Please enter the new expense name:").strip().title()
                    if new_name and all (char.isalpha() or char.isspace() for char in new_name):
                        expense["name"] = new_name.title()
                        save_expenses()
                        show_expense(expense)
                        break
                    else:
                        print("Please enter the name")
            elif choice == "2":
                while True:
                    try:
                        new_amount = float(input("Please enter the new expense amount:"))
                        if new_amount <= 0:
                            print("Amount must be greater than zero")
                            continue
                        expense["amount"] = new_amount
                        print(" Expense amount update successfully")
                        save_expenses()
                        show_expense(expense)
                        break
                    except ValueError:
                        print("Please enter the amount")
            elif choice == "3":
               break
            elif choice=="4":
                return
            else:
                print("Please enter the choice 1,2,3 or 4")

#---------------------------------------------------------------------------------------
def show_expense(expense):
    print("\n---CURRENT EXPENSE---")
    print(f"ID :{expense['id']}\n"
          f"Name :{expense['name']}\n"
          f"Amount :{expense['amount']}\n")
#---------------------------------------------------------------------------------------
def show_all_expenses():
    if not expenses:
        print("No expenses found")
        return
    for expense in expenses:
        show_expense(expense)
#---------------------------------------------------------------------------------------
def delete_expense():
    # select an expense
    expense = select_expense()
    # show the selected expense
    show_expense(expense)
    # Allow repeated delete
    while True:
        chooice_delete = input("do you want to delete the expense ?\n"
                               "1-Yes\n"
                               "2-No(Exit)\n").strip()
        if chooice_delete == "1":
            expenses.remove(expense)
            reassign_expense_id()
            save_expenses()
            print("Expense deleted successfully")
            show_all_expenses()
        elif chooice_delete == "2":
            print("deletion cancelled")
            return
        else:
            print("Please enter the choice 1 or 2")
            continue

#---------------------------------------------------------------------------------------
def select_expense():
#select an expense
 while True:
    try:
        expense_id = int(input("Please enter the expense ID:"))
    except ValueError:
        print("Please enter the ID :")
        continue

    expense = next((item for item in expenses if item["id"] == expense_id), None)
    if expense is not  None:
        return  expense
    print("Expense ID not found . please enter the ID")

#---------------------------------------------------------------------------------------
def reassign_expense_id():
    for index, expense in enumerate(expenses, start=1):
        expense ["id"] = index
