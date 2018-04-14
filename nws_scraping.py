#adding any relevant libraries needed
import requests
from bs4 import BeautifulSoup

#Get the webpage
page = requests.get('https://www.dataquest.io/blog/web-scraping-tutorial-python/')

#Turn into html
soup = BeautifulSoup(page.content, 'html.parser')

#prettify html
print(soup.prettify())

print(soup.find_all('p'))

print(soup.find_all('p')[0].get_text())

print(soup.find_all('p')[-1].get_text())

