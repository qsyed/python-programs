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
        number_of_pages = int(input("how many pages would you like to scrap ? "))
        for n in range(1, number_of_pages+1):
            scraping_url = self.base_url.format(n)
            response = requests.get(scraping_url)
            soup = BeautifulSoup(response.text, "html.parser" )
            books = soup.find_all("article")
            for book in books:
                book_data = (id, self.get_title(book), self.get_price(book), self.get_rating(book))
                all_books.append(book_data)
                id += 1
        
        self.save_to_db(all_books)
        print(all_books)


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

    def view_pro(self):
        self.CRUD_func.view_all_products()

    def searc_item(self):
        self.CRUD_func.search_item()


class CRUD:
    def __init__(self):
        pass

    def view_all_products(self):
        connection = sqlite3.connect("CRUD-sqlite3/books_data.db")
        c = connection.cursor()
        items = c.execute("SELECT * FROM books")
        for item in items:
            print(item)
        connection.commit()
        connection.close()

    def search_item(self):
        connection = sqlite3.connect("CRUD-sqlite3/books_data.db")
        c = connection.cursor()
       
        book_id = input("enter the name of the book ")
        c.execute("""Select * from books WHERE id=?""", (book_id, ))
        rows = c.fetchone()
        print(rows)
       
       

        connection.commit()
        connection.close()






        


test = scraping()
test.scrape()
test.view_pro()
test.searc_item()