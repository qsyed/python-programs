from inven import Inventory
import sys

class Menu:
 
 ''' Displays a list of choices on the terminal for  the user to run '''
 
 
 
 def __init__(self):
 
 
      #instantiate a new manager object
      self.inventor = Inventory() 
 
      #defines the actions the user can perform
      
      self.choices = {
 
           "1" : self.show_items,
 
           "2" : self.create_items,
 
           "3" : self.search_items,

           "4" : self.update_items,

           "5" : self.delete_items,
 
           "Q" : self.quit
 
 
 
        }
 
 
 
 
 
 def display_menu(self):
 
       print(""" 
            **************************
             Welcome to my bookstore!
             How can we help you?  
 
 
             1. Show items
 
             2. Create item
 
             3. Search items

             4. Update items

             5. Delete item
 
             Q. Quit program
 
             """)
 
 
 def run(self):
 
     ''' Display menu and respond to user choices '''
 
     while True:
 
           self.display_menu()
 
           choice = input("Enter an option: " )
 
           action = self.choices.get(choice)
 
           if action:
 
                action()
 
           else:
 
              print("{0} is not a valid choice".format(choice))
 
 
 
 ### Call our Manager Object functions
 
 def show_items(self):
  
   self.inventor.show_items()
 

 def create_items(self):
    task_name = input(f"What is your item's name? \n\n")
    price = int(input("whats the price of the item"))
    self.inventor.create_items(task_name, price)
 
 
 def search_items(self):
    
    self.inventor.search_items()

 def update_items(self):
    item_id = int(input(f"ID of item to update: \n\n"))
    
    self.inventor.update_items(item_id)   

 def delete_items(self):
    item_id = int(input(f"ID of item to delete: \n\n"))
   #  task_id = int(task_id) - 1
    self.inventor.delete_items(item_id)

 def quit(self):

      # choice = input("Do you want to save your session? y/n \n\n")
      
      ''' quit or terminate the program '''
 
      print("Thank you for visiting the bookstore today! \n")
 
      sys.exit(0)