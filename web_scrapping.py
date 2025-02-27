import requests

from bs4 import BeautifulSoup

import pandas as pd


url = "http://books.toscrape.com/"

response = requests.get(url)

# print(response.content)


if response.status_code == 200:

    soup = BeautifulSoup(response.content, "html.parser")

    # print(soup)

    books = soup.find_all("article", class_="product_pod")

    titles = []

    price = []

    Availability = []
    ls = []
    for i in books:

        t = i.h3.a["title"]
        titles.append(t)

        p = i.find("p", class_="price_color").text
        # print(p)
        price.append(p)

        s = i.find("p", class_="instock availability").text.strip()
        # print(s)
        Availability.append(s)
        # json={
        #     "Title":t,
        #     "Price":p,
        #     "Availability":s
        # }
        # ls.append(json)

    # print(titles)
    # print(price)
    # print(Availability)
    # print(ls)
    df = pd.DataFrame({"Title": titles, "Price": price, "Availability": Availability})
    print(df.head(10))
    # else:
    #     print("Failed to retrieve data:", response.status_code)
