#installing packages/dependencies
import urllib3
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#get your url to parse
url = 'https://www.bloomberg.com/markets/stocks'
http = urllib3.PoolManager()

#get the html of the page using urllib
response = http.request('GET', url)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(response.data, "html.parser")

# Take out a part from the html and get the value
name_box = soup.find('td', attrs={'data-type': 'value', 'class': 'data-table-row-cell'})
print(name_box)