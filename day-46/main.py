import requests
from datetime import datetime
from bs4 import BeautifulSoup

def ask_question():
    while True:
        question = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD:")
        try:
            valid_date = datetime.strptime(question, "%Y-%m-%d")
            return question
        except ValueError:
            print("Invalid Forma. Type the date in this format YYYY-MM-DD.")

date = ask_question()

print(f"You have chosen to travel to {date}")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=BILLBOARD_URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


print(song_names)