from bs4 import BeautifulSoup
from urllib import request
from nltk import word_tokenize
import requests 
response = requests.get("https://e.vnexpress.net/news/travel/stranded-in-vietnam-foreign-tourists-find-silver-lining-4339108.html")
conten =  response.text
soup = BeautifulSoup(conten, "html.parser")
span_content = soup.find(name="span", class_="lead_post_detail row").getText()
print(span_content)
div_content = soup.find_all(name="p", class_="Normal")
div_content = [(item.getText()) for item in div_content]
print(div_content)
with open("NoiDung.txt", mode="w") as file:
    file.write(f"{span_content.lower()}")
    for content in div_content:
        file.write(f"{content.lower()}\n")