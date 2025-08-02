from grocery_menu import *
from grocery_list import * 
while True:
    print("1. Create a shopping list")
    print("2. Show item list")
    print("3. Total cost")
    print("4. Compare total against your budget")
    print("5. Complete shopping item")
    print("6. Exit")

    choice = input ("Enter a number: ")

    if choice == "1":
            add_items()
    elif choice == "2":
          show_items()
    elif choice == "3":
          total_cost()
    elif choice == "4":
          total_budget()
    elif choice == "5":
          complete_item()
    elif choice == "6":
          print("Goobye for now!")
          break
    else:
          print("Invalid option!")
        
