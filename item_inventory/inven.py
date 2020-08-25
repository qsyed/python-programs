import sys

class Inventory:
 
  def __init__(self):
    self.all_items = []
    self.latest_id = 0
       
  def create_items(self, item_name, price):
    new_item = Item(self.latest_id, item_name, price)
    self.all_items.append(new_item)
    self.latest_id += 1
    # self.show_items()
  
  def delete_items(self, item_id):
    self.all_items.pop(item_id)
    self.show_items()
    
  def search_items(self):
    search = input("Enter the name of the book you want to look for.")
  
    count = 0
    for item in self.all_items:
      
      if search in item.item_name:

        print("We have it in stock")
        print(f"Item ID: {count}")
      else:
        count +=1
    print("Sorry We dont have the item")
    
  def update_items(self, item_id):
    self.all_items[item_id].price = input("Enter the new price for that book:")
    print(self.all_items[item_id])

  def show_items(self):
    for x in self.all_items:
      print(x)
    # return self.all_items
    print (len(self.all_items))

  def quit(self):
 
    print("Thank you for visiting the warehouse today")
    sys.exit(0)



   
class Item:
  def __init__(self, item_ID, item_name, price):
    self.item_ID = item_ID
    self.item_name = item_name
    self.price = price

  def __str__(self):
    return f"ID:{self.item_ID}, Name: {self.item_name}, Price: {self.price}"