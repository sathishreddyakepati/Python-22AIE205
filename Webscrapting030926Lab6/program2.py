# 2 . i) Fetch only quotes with love/life as tag
#     ii)Fetch all quotes then filtre quotes with tag as love/life


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
quote_blocks = soup.find_all("div", class_="quote")
#i)
completeData = []
for block in quote_blocks:
    text = block.find("span", class_="text").text
    author = block.find("small", class_="author").text
    tags = []
    for tag in block.find_all("a", class_="tag"):
        tags.append(tag.text)
    # print(text," - ",author," - ",tags)
    for tag in tags:
        if(tag=="love"):
            completeData.append([text,author,tags])

        
    

df = pd.DataFrame(completeData, columns=["Quote","Author","Tags"])
print(df)