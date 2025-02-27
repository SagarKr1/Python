import requests

from bs4 import BeautifulSoup

url = "https://www.rottentomatoes.com/browse/movies_in_theaters"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup)

movies=soup.find_all("div", class_="flex-container")
# print(movies)
title=[]

for i in movies:
    # print(i)
    t=i.find('span',class_="p--small").text.strip()
    # print(t)
    title.append(t)
    
print(title)