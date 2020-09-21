from crud_app import scraping
import sys

class Menu:
    def __init__(self):
        self.app = scraping()
        self.options = {

      "1": self.scrape,

      "2": self.view_products,

      "3": self.search_item,

      "4": self.search_item_rating,

      "5": self.update_item,

      "6": self.delete_item,

      "7": self.quit


    }
      

    def display_options(self):

        print(""" 
                ************* MAIN MENU *************
                WElcome to the Book Store !!! 

                Please choose one of the options below:
    
                1. SCRAPE ITEMS TO DATA BASE 
    
                2. See All Products
    
                3. Search For An Item By ID

                4. Search For An Item By Rating

                5. Update Item

                6. Delete Item

                7. QUIT 

                                  
                """)




    def scrape(self):
        self.app.scrape()
        

    def view_products(self):
        self.app.view_products()
        
 
    def search_item(self):
        self.app.search_item()

    def search_item_rating(self):
        self.app.search_item_rating()
    
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
