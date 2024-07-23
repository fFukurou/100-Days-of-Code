import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
web_page = requests.get(URL).text

soup = BeautifulSoup(web_page, "html.parser")

titles = [f"{title.getText()}\n" for title in soup.find_all(name="h3", class_="title")]
titles.reverse()

with open ("Day-45/100_Movies/movies.txt", "w", encoding="utf8") as file:
    file.writelines(titles)
