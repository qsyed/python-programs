import requests 
from bs4 import BeautifulSoup 
from random import choice
from csv import DictReader

base_url = "http://quotes.toscrape.com"


'''
Leave csv in original file loctaion 


'''

def read_quotes(filename):
    with open(filename, 'r') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)



def start_game(quotes):

    quote = choice(quotes)
    print("Here's a quote: ")
    print(quote['text'])
    print(quote['author'])

    remaining_guess = 4
    guess = ' '

    while guess.lower() != quote['author'].lower() and remaining_guess > 0:
        guess = input (f'Who said this quote? Guesses remaining {remaining_guess} ')

        if guess.lower() == quote['author'].lower():

            print("YOU ARE CORRECT !!!")
            break

        remaining_guess -= 1
        if remaining_guess == 3:
            res = requests.get(f'{base_url}{quote["bio-link"]}')
            soup = BeautifulSoup(res.text, 'html.parser')
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
        elif remaining_guess == 2:
            first_initial = quote['author'][0]
            print(f"The author's first name starts with {first_initial}")
        elif remaining_guess == 1:
            last_initial = quote['author'].split(" ")[1][0]
            print(f"The author's first name starts with {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")



    again = " "
    while again.lower() not in ('y', 'yes', 'no', 'n'):
        again = input("Would you like to play again (y/n)?")

    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("ok bye")

quotes = read_quotes("quotes.csv")
start_game(quotes)