import requests 
from bs4 import BeautifulSoup as bs 

r = requests.get('Enter Website')      # Load webpage 
soup = bs(r.content)                   # Pull site content
print(soup.prettify())                 # Print

# Below, we will specifically be navigating a HTML document. 

bs.Stylesheet()    # Returns all info in <style> tags from CSS Stylesheet in HTML document. 
bs.Script()        # For items in <script> tags, Javascript items. 
bs.Template()      # For HTML templates, that is, items between <template> tags.


