import requests 
from bs4 import BeautifulSoup as bs 

r = requests.get('Enter Website')      # Load webpage 
soup = bs(r.content)                   # Pull site content
print(soup.prettify())                 # Print

