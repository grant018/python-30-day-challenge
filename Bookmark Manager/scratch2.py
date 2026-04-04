import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.unz.com")
soup = BeautifulSoup(response.text, "html.parser")

with open("site.txt", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
