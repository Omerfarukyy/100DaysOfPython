import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
res = response.text

soup = BeautifulSoup(res, "html.parser")
titles = [title.string for title in soup.findAll("h3", class_="title")]
# these are for UnicodeEncodeError
titles[15] = "85) Leon"
titles[41] = "59) E.T. The Extra Terrestrial"

titles = titles[::-1]
print(titles)
with open("movies.txt", "w") as file:
    file.write("\n".join(titles))
