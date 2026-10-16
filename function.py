expenses = []

#=============== ADD EXPENSES ===============

def add_expense():
    while True:
        try:
            expense_count = int(input("How many Expenses do you want to add? : "))
            if expense_count > 0:
                break
            else:
                print("please enter the number")
        except ValueError:
            print("please enter the number")
    for i in range(expense_count):
        print(f"\nAdding expense {i + 1} of {expense_count}")

        while True:
            expense_name = input("please enter the expense name:").strip().title()

            if expense_name and all(char.isalpha() or char.isspace()for char in expense_name):
                break
            else:
                print("please enter the name")

        while True:
            try:
                expense_amount = float(input("please enter the expense amount: "))
                if expense_amount > 0:
                    break
                else:
                    print("amount must be greater than zero")
            except ValueError:
                print("please enter the number")
        # Assign an ID that does not conflict with existing expenses
        expense = {
            "id": max((item["id"] for item in expenses), default=0) + 1,
            "name": expense_name,
            "amount": expense_amount
        }
        expenses.append(expense)
        save_expenses()
        print("Expense added successfully")

    show_all_expenses()

#=============== FILE PERSISTENCE ===============

def save_expenses():
    # Rewrite the file so it always reflects the current expense list.
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['id']},{expense['name']},{expense['amount']}\n")

def load_expenses():
    expenses.clear()
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",", 2)

                # Ignore records that do not match the expected format.
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
        # A missing file is expected when the program runs for the first time .
        print("expenses.txt file not found")

#=============== EDIT EXPENSE ===============

def edit_expense():
    if not has_expenses():
        return

    # Keep the selection active when the user wants to edit another expense
    show_expense_ids_and_name()
    expense = select_expense()
    if expense is None:
        return

    show_expense(expense)

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
                if new_name and all(char.isalpha() or char.isspace() for char in new_name):
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

        elif choice == "4":
            return

        else:
            print("Please enter the choice 1,2,3 or 4")

#=============== DISPLAY EXPENSE ===============

def show_expense(expense):
    print("\n---CURRENT EXPENSE---")
    print(f"ID :{expense['id']}\n"
          f"Name :{expense['name']}\n"
          f"Amount :{expense['amount']}\n")

def show_all_expenses():
    if not has_expenses():
        return
    for expense in expenses:
        show_expense(expense)

def show_expense_ids_and_name():
    if not has_expenses():
        return
    print("IDs and Name:")
    for expense in expenses:
        print(f"{expense['id']}- {expense['name']}")

#=============== DELET EXPENSE ===============

def delete_expense():
    if not has_expenses():
        return
    show_expense_ids_and_name()
    # select an expense
    expense = select_expense()
    if expense is None:
        return
    # show the selected expense
    show_expense(expense)
    # Allow repeated delete
    while True:
        choice_delete = input("do you want to delete the expense ?\n"
                              "1-Yes\n"
                              "2-No(Exit)\n").strip()
        if choice_delete == "1":
            expenses.remove(expense)
            reassign_expense_id()
            save_expenses()
            print("Expense deleted successfully")
            show_all_expenses()
            return
        elif choice_delete == "2":
            print("deletion cancelled")
            return
        else:
            print("Please enter the choice 1 or 2")
            continue

#=============== EXPENSE SELECTION ===============

def select_expense():
    if not has_expenses():
        return

    while True:
        try:
            expense_id = int(input("Please enter the expense ID:"))
        except ValueError:
            print("Please enter the ID :")
            continue

        expense = next((item for item in expenses if item["id"] == expense_id), None)
        if expense is not None:
            return expense
        print("Expense ID not found . please enter the ID")

def reassign_expense_id():
    # Keep IDs sequential after an expense is removed.
    for index, expense in enumerate(expenses, start=1):
        expense["id"] = index

#=============== EXPENSE CALCULATIONS ===============

def total_expense():
    if not has_expenses():
        return
    while True:
        total = 0
        valid_ids = True
        choose = input("Calculate all expenses or select specific one ?\n(1-ALL/2-SELECT/3-EXITE)\n").strip()
        if choose == "1":
            for expense in expenses:
                total += expense["amount"]
            print(f"Total : {total}")
        elif choose == "2":
            show_all_expenses()
            selected_id = input(
                "Please enter the IDs of expenses you want to add together:").strip().split(" ")
            for item in selected_id:
                try:
                    expense_id = int(item)
                except ValueError:
                    print(f" Invalid ID {item}")
                    valid_ids = False
                    break

                found = False

                for expense in expenses:
                    if expense["id"] == expense_id:
                        total += expense["amount"]
                        found = True
                        break

                if not found:
                    print(f"Expense ID {expense_id} was not found")
                    valid_ids = False
                    break

            if valid_ids:
                print(f"Total : {total}")

        elif choose == "3":
            break
        else:
            print("Please enter the choice 1 , 2 or 3")

def show_highest_and_lowest_expensive():
    if not has_expenses():
        return

    highest_expensive = max(expenses, key=lambda expense: expense["amount"])
    lowest_expensive = min(expenses, key=lambda expense: expense["amount"])
    print("-->> HIGHEST EXPENSE <<--", end="")
    show_expense(highest_expensive)

    print("-->> LOWEST EXPENSE <<--", end="")
    show_expense(lowest_expensive)

#=============== VALIDATION HELPERS ===============

def has_expenses():
    if not expenses:
        print("There are no expense")
        return False
    return True


