#Importing necessary modules
import urllib
import urllib3
import requests
import pandas as pd
from bs4 import BeautifulSoup

#get the webpage + html
page = requests.get('https://www.facebook.com/danish.lookmanjee')
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
userNames = soup.find_all('h1')
print(len(userNames))
print(userNames)