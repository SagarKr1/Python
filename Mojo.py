import requests

from bs4 import BeautifulSoup

url = "https://www.boxofficemojo.com/date/?ref_=bo_nb_wey_secondarytab"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers)

print(response)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup)

movies=soup.find_all('td', class_='a-text-left mojo-field-type-release mojo-cell-wide')
# print(movies)
title=[]

for i in movies:
    # print(i)
    data = i.find('a',class_="a-link-normal").text.strip()
    # print(data)
    title.append(data)
print(title)