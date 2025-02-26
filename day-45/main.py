import os
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

url = response.text
    
soup = BeautifulSoup(url, 'html.parser')

hacker_news_post_links = soup.select("a", class_="titleline")

for link in hacker_news_post_links: 
    print(link.get("href"))