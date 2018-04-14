#importing the necessary packages
import requests
from bs4 import BeautifulSoup
import re

#Get the page and html
webpage = requests.get('https://www.etsy.com/?utm_source=google&utm_medium=cpc&utm_term=etsy_exact&utm_campaign=Search_US_Brand_Google_HP_General-Brand_Core_General_Exact[B]&utm_ag=A1&utm_custom1=7915eeea-5660-46ea-b64d-f83502b8c4e2&gclid=EAIaIQobChMItIir8LKx2gIVQZppCh1MHQwHEAAYASAAEgKiO_D_BwE')
soup = BeautifulSoup(webpage.text, 'html.parser')

#print status code
print(webpage.status_code)

#print prettified version of the page
#print(soup.prettify())

#Getting most popular items
items = soup.find_all('span', attrs={'class':'vesta-hp-category-title vesta-hp-curated-category ml-xs-2 ml-sm-0 position-relative '})
print(len(items))

for item in items:
    print(item.get_text())

homeLiving = soup.find_all('div', attrs={'height': '21px;'})
print(homeLiving)