import sqlite3
import requests
from bs4 import BeautifulSoup


base_url = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape():
    number_of_pages = int(input("how many pages would you like to scrap ? "))
    for n in range(1, number_of_pages+1):
        scraping_url = base_url.format(n)
        print(scraping_url)


scrape()