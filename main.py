import function as expense_manager
expense_manager.load_expenses()

while True:
    choise_option = input("please choose an option(just write the number):\n"
                         "1-Add Expense\n"
                         "2-Show Expense\n"
                         "3-Edit Expense\n"
                         "4-Delete Expense\n"
                         "5-Show Total Expense\n"
                         "6-Show Highest And Lowest Expense\n"
                         "7-Exit\n")
    if choise_option.isdigit():

        if 1 <= int(choise_option) <= 7:

            if choise_option == "1":
                expense_manager.add_expense()
            elif choise_option == "2":
                expense_manager.show_all_expenses()
            elif choise_option == "3":
                expense_manager.edit_expense()
            elif choise_option == "4":
                expense_manager.delete_expense()
            elif choise_option == "5":
                expense_manager.total_expense()
            elif choise_option == "6":
                expense_manager.show_highest_and_lowest_expensive()
            elif choise_option == "7":
                print("Thank you for using this program\nGoodbye!")
                break
        else:
            print("number must be between 1 and 7")

    else:
        print("please enter a number ")
