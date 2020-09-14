import sqlite3
import requests
from bs4 import BeautifulSoup


base_url = "http://books.toscrape.com/catalogue/page-{}.html"


all_books = []
def scrape():
    number_of_pages = int(input("how many pages would you like to scrap ? "))
    for n in range(1, number_of_pages+1):
        scraping_url = base_url.format(n)
        response = requests.get(scraping_url)
        soup = BeautifulSoup(response.text, "html.parser" )
        books = soup.find_all("article")
        for book in books:
            book_data = (get_title(book), get_price(book), get_rating(book))
            all_books.append(book_data)


def get_title(book):
    return book.find("h3").find("a")['title']

def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("Â","").replace("£",""))

def get_rating(book):
    paragraph = book.select(".star-rating")[0]
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5 }
    word = paragraph.get_attribute_list("class")[-1]
    return ratings[word]


def save_to_db(all_books):
    connection = sqlite3.connect("CRUD-sqlite3/books_data.db")
    c = connection.cursor()
    c.execute("DROP TABLE books")
    c.execute('''CREATE TABLE books 
        (title TEXT, price REAL, rating INTEGER)''')

    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    connection.commit()
    connection.close()

scrape()
print(all_books)
save_to_db(all_books)