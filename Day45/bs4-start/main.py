from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc = response.text
soup = BeautifulSoup(yc, "html.parser")

text_soup = soup.findAll("span", class_="titleline")
article_texts = [s.a.string for s in text_soup]

score_soup = soup.findAll("span", class_="score")
article_upvotes = [int(s.string.split()[0]) for s in score_soup]

link_soup = soup.findAll("span", class_="titleline")
article_links = [(s.a["href"]) for s in link_soup]
print(article_upvotes)
max = 0
for index in range(len(article_upvotes)):
    if article_upvotes[index] > article_upvotes[max]:
        max = index
print(article_texts[max])
print(article_links[max])
print(article_upvotes[max])
# import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
#
# all_tags = soup.findAll(name="a")
#
# for tag in all_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
# s_h = soup.find(name="h3",class_="heading")
# print(s_h)
# com= soup.select_one(selector="p a")
