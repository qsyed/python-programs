from crud_app import scraping
import sys

class Menu:
    def __init__(self):
        self.app = scraping()
        self.options = {

      "1": self.scrape,

      "2": self.view_products,

      "3": self.search_item,

      "4": self.update_item,

      "5": self.delete_item,

      "6": self.quit


    }
      

    def display_options(self):

        print(""" 
                ************* MAIN MENU *************
                WElcome to the Book Store !!! 

                Please choose one of the options below:
    
                1. SCRAPE ITEMS TO DATA BASE 
    
                2. See All Products
    
                3. Search For an Item 

                4. Update Item

                5. Delete Item

                6. QUIT 

                                  
                """)




    def scrape(self):
        self.app.scrape()
        

    def view_products(self):
        self.app.view_products()
        
 
    def search_item(self):
        self.app.search_item()
    
    def update_item(self):
        self.app.update_item()

    def delete_item(self):
        self.app.delete_item()
        

    def quit(self):
        self.app.quit()
        sys.exit(0)
     
       
    
    def run(self):

        while True:
            self.display_options()
            option = input("Enter an option: ")
            action = self.options.get(option)

            if action:
                action()
            else:
                print("{0} is not a valid option, Please try again".format(option))

if __name__ == "__main__":
  Menu().run()
