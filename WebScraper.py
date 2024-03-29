import requests
from bs4 import BeautifulSoup as bs 

r = requests.get('Enter Website')      # Load webpage 
soup = bs(r.content)                   # Pull site content
print(soup.prettify())                 # Print

# Below, we will specifically be navigating a HTML document. 

bs.Stylesheet()    # Returns all info in <style> tags from CSS Stylesheet in HTML document. 
bs.Script()        # For items in <script> tags, Javascript items. 
bs.Template()      # For HTML templates, that is, items between <template> tags.

# The following commands are for XML documents

bs.Declaration()             # Represents declaration at the beginning of XML document.
bs.Doctype()                 # Document Type Declaration at beginning of XML file. 
bs.CData()                   # Pulls CData from XML. 
bs.ProcessingInstruction()   # Represents contents of XML processing instruction.

# Note: <span> for content. 

# Determining tag type by calling type() method.
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
type(tag)


