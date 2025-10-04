
import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

movies_title_tag = soup.select("div h3.title")

titles = [movie.getText() for movie in movies_title_tag][::-1]



with open("movies.txt", "w",encoding="utf-8") as file:
    for title in titles:
        file.write(title + "\n")
    print("titles added to movies.txt!")






