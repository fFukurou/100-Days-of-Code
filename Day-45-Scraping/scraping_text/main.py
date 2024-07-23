from bs4 import BeautifulSoup   


with open ("Day-45/scraping/website.html", encoding="utf8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText()) #type: ignore
print(section_heading.get("class")) #type: ignore

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)