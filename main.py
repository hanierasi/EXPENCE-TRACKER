from function import *
load_expenses()
while True:
    chose_option = input("please choose an option(just write the number): \n"
                         "1-Add Expense "
                         "2-Show Expense "
                         "3-Edit Expense "
                         "4-Delete Expense "
                         "5-Show total Expense "
                         "6-Sow most Expense "
                         "7-Exit\n")
    if chose_option.isdigit():

        if 1 <= int(chose_option) <= 7:

            if chose_option == "1":
              add_expense()
            elif chose_option == "2":
                pass
            elif chose_option == "3":
                pass
            elif chose_option == "4":
                pass
            elif chose_option == "5":
                pass
            elif chose_option == "6":
                pass
            elif chose_option == "7":
                pass
            else:
                pass
        else:
            print("number must be between 1 and 7")

    else:
        print("please enter a number ")
