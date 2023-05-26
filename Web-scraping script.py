# Web scraping with BeautifulSoup4

import requests
from bs4 import BeautifulSoup
import lxml

# Get the HTML content of the page
page = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'lxml')

# Get the table with the movies
table = soup.find('tbody', class_='lister-list')

# Get the rows of the table
rows = table.find_all('tr')

# Get the title, year, rating and link of each movie
for row in rows:
    title = row.find('td', class_='titleColumn').a.text
    year = row.find('td', class_='titleColumn').span.text
    rating = row.find('td', class_='ratingColumn imdbRating').strong.text
    link = row.find('td', class_='titleColumn').a['href']
    print(title, year, rating, link)
