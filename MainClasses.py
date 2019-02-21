#This file contains the main two classes for the grocery app. One class creates objects for the main shopping list - a list of stores. 
#The other class creates grocery items. Each grocery item must be connected to a store destination.
#from ActionClass import *
#from GroceryApp import *

class GroceryItem(): 
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price 
        self.quantity = quantity
    def view_items_easily(self): #This method displays the grocery items in a simpler format
        print(", ".join([self.item, str(self.price), str(self.quantity)]))
        
class ShoppingList(): 
    def __init__(self, store_name, store_address):
        self.store_name = store_name
        self.store_address = store_address
        self.items_list = []
    def add_item(self, lolhehe): #Every time a grocery object is formed, this method will add it to the according store
        self.items_list.append(lolhehe)

