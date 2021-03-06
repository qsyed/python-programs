# python-programs

## API Project
> This application uses the alpha vantage api to create an investment app similar to acorns and robinhood. A user can register for a unique account and proceed  to buy and sell stocks with real time stock pricing information. Upon creation of  a users account, they are asked how much they want to put into their account in order to buy stocks. Within the program there is logic to calculate how much profit, if any a user has made. Upon exiting the application the data of all existing users and their portfolio is saved to an AWS s3 bucket in the form of a json file.

## CRUD-sqlite3
> This project utilizes the python libraries BeautifulSoup, sqlite3, and requests. A user can input how many pages of data from the website [Books to scrape](https://books.toscrape.com/) The program gets every book's title, price, and rating and saves it to an sqlite database. From the command line a user can start to use the promoted commands to interact with the database. A user can delete, update, and search for specific items. 
 
## flask/book_store
> some of the python libraries BeautifulSoup, Flask, boto3, and sys. This project scraps the website [Books to scrape](https://books.toscrape.com/) and saves the content to a s3 bucket and as a json file. Flask is used in this project create asimple front end interface were users can interact with the scrapped data. 


## flask/to_do_manager 
> this python program is a simple CRUD app using Flask. this was a code along from [freeCodeCamp.org](https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=2482s)


## Hacker-rank 
> My solutions to hacker rank problems

## Item Inventory
> This is a simple CRUD application that mimics a warehouse. A user can add items into inventory. Inorder to create an item a user must pass in the item name and price, when added into inventory the program will create a unique id to track the item. Once created, users can manipulate the items that are in inventory.

 ## leetcode
> my solutions to leetcode problems 

## playlist 
> this is a simple python program that is meant to resammble the backend services of an application like spotify. Essetianly this CRUD app allows a user to create a playlist of songs that they like. 

## regex/parsing_urls 
> a simple regex that parses a given url. the program will group the url into appopraiate tags like: Protocol, Domain, stac. and will print it out. this was a code along from [Colt Steele's python course](https://www.udemy.com/course/the-modern-python3-bootcamp/)


## regex/regular express 
> a simple regex that will parse a given postfix expression. the program will return the different parts of postfix expression. 

## regex/validating_phone_numbers
> a simple regex that parses phone numbers and verifys that they are indeed actual phone numbers. this was a code along from [Colt Steele's python course](https://www.udemy.com/course/the-modern-python3-bootcamp/)


## requests 
> In this section i learned how to use the requests python module to make http requests. in this section a downloaded files, and images using the request module.



## Rock Paper Scissor
> This simple app allows mutiple users to play the well known game, Rock-Paper-Scissor through a command line interface. The leaderboard of the game is saved upon quiting the app, and saved to an s3 bucket.



## sqlite3-python 
> In this section I learn how to connect to an sqlite database and do things such as instertion, bulk insertion, selecting items, and data valiadation. this section is from the [Colt Steele's python course](https://www.udemy.com/course/the-modern-python3-bootcamp/)


## web_scraping/books_to_scrap
> This is a simple CRUD applicaton. A user provides how many number of pages of data they want to extract from a webiste. Once the content of the website is scrapped its placed into a json file. A user can interact with the data that was extracted and can manipulate the data. upon quiting the program the scrapped data is placed in an s3 bucket.


## web_scraping/guessing_game 
> This is a code along from [Colt Steele's python course](https://www.udemy.com/course/the-modern-python3-bootcamp/). In this section I leanrned how to scrap the website [quotes to scrape](http://quotes.toscrape.com/). In the csv_scraper.py file, the program extracts the quote, author, and a link to the quote and places into a csv file. In the game.py file, the program contains the logicc for a simple guessing game. the program choices a random quote and prompts the user to enter the name of the author. The program gives you four chances to get the name of the author correct, providing hints each time you get an attempt wrong. 

 
 
