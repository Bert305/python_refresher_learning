

from bs4 import BeautifulSoup
import requests

page_to_scrape = 'http://quotes.toscrape.com/'
soup = BeautifulSoup(requests.get(page_to_scrape).content, 'html.parser')
quotes = soup.find_all('span', class_='text') # <span> tags with class 'text'
authors = soup.find_all('small', class_='author') # <small> tags with class 'author'


# print the quotes
for quote in quotes:
    print(quote.text)
    
# print the authors
for author in authors:
    print(author.text)