from MainClasses import GroceryItem, ShoppingList
from ActionClass import MenuActions



def main_menu():
    menu_actions = MenuActions()
    user_input = ''
    while user_input != "6":
        user_input = input("What action do you want to perform? \n 1: Add shopping destination \n \
2: Add grocery item \n 3: View current items \n 4: Delete a store or grocery item \n 5: Find total of overall list or store total \n 6: Quit the application \n Your selection: ")
        if user_input == "1":
            menu_actions.add_shopping_list()
        elif user_input == "2":
            menu_actions.add_grocery_item()
        elif user_input == "3":
            menu_actions.view_items()
        elif user_input == "4":
            menu_actions.delete_screen()
        elif user_input == "5":
            menu_actions.totals()

main_menu()