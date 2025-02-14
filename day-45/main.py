import os
from bs4 import BeautifulSoup

file_path = "day-45/website.html"
with open(file_path) as file:
    data = file.read()
    
soup = BeautifulSoup(data, 'html.parser')

print(soup.prettify())