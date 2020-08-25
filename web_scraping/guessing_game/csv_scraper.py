import requests 
from bs4 import BeautifulSoup 
from time import sleep
from random import choice
from csv import DictWriter
# the first two modules above must be intsalled using pip command


# base url 
base_url = "http://quotes.toscrape.com"





def scrap_quotes():
    all_quotes = []
    # next page; to be add to to base url to scrap next page
    url = "/page/1"
    while url:

        response = requests.get(f'{base_url}{url}')
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"Now scrapping {base_url}{url} ")

        # print(soup.body)

        # looking at html class quote to isolate content
        quotes = soup.find_all(class_="quote")


        for quote in quotes:
            all_quotes.append({
                'text': quote.find(class_="text").get_text(),
                'author': quote.find(class_="author").get_text(),
                'bio-link': quote.find('a')['href']
            })

        next_page = soup.find(class_='next')
        url = next_page.find('a')['href'] if next_page else None
        sleep(1)
    return all_quotes



#write quotes to csv file
def write_quotes(quotes):
    with open("quotes.csv", 'w') as file:
        headers = ['text', 'author', 'bio-link']
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrap_quotes()
write_quotes(quotes)
