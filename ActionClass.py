from MainClasses import *
#from GroceryApp import shopping_objects
#from GroceryApp import *

shopping_objects = [] 

class MenuActions():
    def __init__(self):
        pass
    
    def shopping_object_to_string(self, shopping_objects): #This method creates a list of shopping destinations, so when the user wants to add a grocery item, they can choose from a list of stores
        final_list = []
        for x in shopping_objects:
            final_list.append(x.store_name)
        return final_list
                

    def add_shopping_list(self):
        store_list = ", ".join(self.shopping_object_to_string(shopping_objects))
        shop_input = input("Current stores added: " + store_list + "\nWhat's the shopping destination you want to add? ")
        shop_address = input("What's the address of the store? ")
        shop_input_1 = ShoppingList(shop_input, shop_address)
        shopping_objects.append(shop_input_1)


    def add_grocery_item(self):
        if not self.shopping_object_to_string(shopping_objects):
            print("Please add a shopping destination before adding a grocery item.")
            return
        store_list = ", ".join(self.shopping_object_to_string(shopping_objects))
        store_input = input("Current stores added: " + store_list + "\nWhat store do you want to add the item to? ")
        while store_input not in self.shopping_object_to_string(shopping_objects): #Making sure the item is added to a specific store 
            store_input = input("Please add grocery item to one of the following stores: " + store_list +  "\nYour selection: ")
        item_input = input("What item do you want to add? ")
        while True: #making the price and quantity added are actually numbers...
            try:
                price_input = float(input("What price is your item? "))
                quantity_input = int(input("How many of that item do you want to buy? "))
                added_item = GroceryItem(item_input, price_input, quantity_input)
                break
            except:
                print("Please enter a correct price and quantity.")

        for x in shopping_objects: #loops through the list of stores. if the store name matches the input the user put, then the grocery object is added to that specific store object
            if x.store_name == store_input:
                x.add_item(added_item)

    def view_items(self): #prints the store, followed by the items for that store
        shopping_list = self.shopping_object_to_string(shopping_objects)
        if not shopping_list:
            print("No current items to view. Going back to main menu.")
            return
        for x in shopping_objects:
            print("Store: " + x.store_name)
            print("Address: " + x.store_address)
            counter = 1
            for item in x.items_list:
                print(f"{str(counter)}) ", end="")
                item.view_items_easily()
                counter +=  1

    def totals(self):
        if not shopping_objects:
            print("No current items to total. Going back to main menu.")
            return
        user_selection = input("Would you like to see your 1) Item total or 2) Store Total? ")
        while user_selection not in ["1","2"]:
            user_selection = input("Please enter either 1 for Item Total or 2 for Store Total")
        total = 0
        if user_selection == "1":
            for x in shopping_objects:
                for item in x.items_list:
                    total = total + item.price * item.quantity
            print(f"Your overall total is {total}. Returning to main menu.")
            return
        elif user_selection == "2":
            store_list = ", ".join(self.shopping_object_to_string(shopping_objects))
            store_input = input("Current stores added: " + store_list + "\nWhich store do you want to find the total of? ")
            while store_input not in self.shopping_object_to_string(shopping_objects):
                store_input = input("Please choose one of the stores shown.")
            for x in shopping_objects:
                if x.store_name == store_input:
                    if not x.items_list:
                        print("No current items to total. Going back to main menu.")
                        return
                    for item in x.items_list:
                        total = total + item.price * item.quantity
                    print(f"Your total for {store_input} is {total}. Returning to main menu.")
                    return


    def delete_screen(self): #asks the user if he/she wants to delete store or grocery item
        input_choice = input("Do you want to delete a store or a grocery item? Select the number below: \n 1) Store \n 2) Grocery Item \n Your selection: ")
        while input_choice not in ["1","2"]:
            input_choice = input("Please choose one of the following: \n 1) Store \n 2) Grocery Item \n Your selection: ")
        if input_choice == "1":
            self.delete_shopping_list()
        elif input_choice == "2":
            self.delete_grocery_item()


    def delete_shopping_list(self): #deletes a specified store name
        if not shopping_objects:
            print("No current items to delete. Going back to main menu.")
            return
        store_list = ", ".join(self.shopping_object_to_string(shopping_objects))
        store_input = input("Current stores added: " + store_list + "\nType the name of the store you want to remove from the list. If none, press Q. (Warning: All items from that store will be deleted)  \n Your Selection: ")
        while store_input not in self.shopping_object_to_string(shopping_objects):
            store_input = input("Please choose one of the stores shown.")
        if store_input == "Q":
            return
        for x in range(len(shopping_objects)):
            if shopping_objects[x].store_name == store_input:
                del shopping_objects[x]
                print(f"{store_input} has been deleted. Going back to main menu now.")
        return

    def delete_grocery_item(self): #deletes a specified grocery item    
        if not shopping_objects:
            print("No current items to delete. Going back to main menu.")
            return
        store_list = ", ".join(self.shopping_object_to_string(shopping_objects))    
        store_input = input("Current stores added: " + store_list + "\nWhich store do you want to delete a grocery item from? ")
        while store_input not in self.shopping_object_to_string(shopping_objects):
            store_input = input("Please choose one of the stores shown.")
        counter = 1 #This counter displays the numbers for the list (ex. 1) eggs 2) bread
        if store_input == "Q":
            return 
        for x in shopping_objects:
            if x.store_name == store_input:
                if not x.items_list:
                    print("No current items to delete. Going back to main menu.")
                    return
                for item in x.items_list:
                    print(f"{str(counter)}) ", end="")
                    item.view_items_easily()
                    counter +=  1
        while True:
            try:  
                del_item = int(input(f"Here are the current items for {store_input}. Type the number of the item you want to delete. If none, press Q. "))
                for x in shopping_objects:
                    if x.store_name == store_input:
                        del x.items_list[del_item - 1]
                break
            except IndexError:
                print("Please choose an item number on the list.")
            except:
                print("Please enter an integer.")
            
        print("Item has been deleted. Going back to main menu.") 
        return

