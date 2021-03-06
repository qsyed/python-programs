import sqlite3
import requests
from bs4 import BeautifulSoup




class scraping:

    def __init__(self):
        self.base_url = base_url = "http://books.toscrape.com/catalogue/page-{}.html"
        self.CRUD_func = CRUD()


    def scrape(self):
        all_books = []
        id = 0
        print("there are 50 pages on the site: ")
        number_of_pages = int(input("how many pages would you like to scrap ? "))
        

        if number_of_pages > 0 and number_of_pages <= 50:
            print("This may take a while hang in there")
            for n in range(1, number_of_pages+1):
                scraping_url = self.base_url.format(n)
                response = requests.get(scraping_url)
                soup = BeautifulSoup(response.text, "html.parser" )
                books = soup.find_all("article")
                for book in books:
                    book_data = (id, self.get_title(book), self.get_price(book), self.get_rating(book))
                    all_books.append(book_data)
                    id += 1
            print("the items have been saved into the data base")
        else:
            print("enter a number between 1 and 50")
            return
        
       
        
        self.save_to_db(all_books)
        # print(all_books)


    def get_title(self, book):
        return book.find("h3").find("a")['title']

    def get_price(self, book):
        price = book.select(".price_color")[0].get_text()
        return float(price.replace("Â","").replace("£",""))

    def get_rating(self, book):
        paragraph = book.select(".star-rating")[0]
        ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5 }
        word = paragraph.get_attribute_list("class")[-1]
        return ratings[word]


    def save_to_db(self, all_books):
        connection = sqlite3.connect("CRUD-sqlite3/books_data.db")
        c = connection.cursor()
        c.execute("DROP TABLE books")
        c.execute('''CREATE TABLE books 
            (id INTEGER, title TEXT, price REAL, rating INTEGER)''')

        c.executemany("INSERT INTO books VALUES (?,?,?,?)", all_books)
        connection.commit()
        connection.close()

    def view_products(self):
        self.CRUD_func.view_all_products()

    def search_item(self):
        self.CRUD_func.search_item()
    
    def search_item_rating(self):
        self.CRUD_func.search_item_rating()

    def update_item(self):
        self.CRUD_func.update()
    
    def delete_item(self):
        self.CRUD_func.delete()

    def quit(self):
        self.CRUD_func.quit()

class CRUD:
    def __init__(self):
        self.connection  = sqlite3.connect("CRUD-sqlite3/books_data.db")
        self.c = self.connection.cursor()

    def view_all_products(self):
        items = self.c.execute("SELECT * FROM books")
        for item in items:
            print(item)
       

    def search_item(self):
        
        book_id = input("enter the id of item you want to view ")
        self.c.execute("""Select * from books WHERE id=?""", (book_id, ))
        rows = self.c.fetchone()
        print(rows)
        
    

    def search_item_rating(self):
        rating = input("enter the rating to search by ")
        int_rating = int(rating)
        if int_rating <= 5:
            self.c.execute("""Select * from books WHERE rating=?""", (rating, ))
            rows = self.c.fetchall()
            for row in rows:
                print(row)
        else:
            print("Books are rated on a scale of 1 through 5.")
            print("please enter a valid number")
        
        


    def update(self):

        
        book_id = input("enter the id of the book to update ")
        
        title = input("enter the new title: ")
        price = float(input("enter the new price: "))
        rating = int(input("enter the new rating: "))
        
        if isinstance(price, float) and isinstance(rating, int):
            if rating >= 0 and rating <= 5:
                self.c.execute("""UPDATE books SET title=?, price=?, rating=? WHERE id=? """, (title, price, rating, book_id))
                print("*****************************************************")
                print(" ")
                print("the book has been saved !!!")
                print(" ")
                print("*****************************************************")

                self.c.execute("""SELECT id, title, price, rating FROM books WHERE id=?""", (book_id, ))
                rows = self.c.fetchone()
                print(rows)

            else:
                print("make sure that that you pass in the correct information")
                print("the rating scale is from 1 through 5")
        self.connection.commit()
        
   

    def delete(self):
        book_id = input("enter the id of the book to delete ")

        self.c.execute("""DELETE FROM books WHERE id=?""", (book_id, ))



        print("*****************************************************")
        print(" ")
        print("the book has been deleted !!!")
        print(" ")
        print("*****************************************************")
        self.connection.commit()




        


    def quit(self):
        
        self.connection.close()




        

