import requests

from bs4 import BeautifulSoup

import pandas as pd


# Amazon iPhone Search URL

url = "https://www.amazon.in/s?k=iphone+16"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# Send request

response = requests.get(url, headers=headers)

print(response)

soup = BeautifulSoup(response.content, "html.parser")

# print(soup)


# # Extracting product details

products = soup.find_all("div", {"data-component-type": "s-search-result"})

# print(products)

data = []

for i in products:

    title = i.h2.text.strip()

    price = i.find("span", "a-price-whole")

    rating = i.find("span", "a-icon-alt")

    price = price.text.strip() if price else "N/A"

    rating = rating.text.strip() if rating else "N/A"

    data.append({"Product": title, "Price": price, "Rating": rating})


# Convert to DataFrame

df = pd.DataFrame(data)

print(df)
