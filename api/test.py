import requests
from bs4 import BeautifulSoup

def getAmazonProducts(query):
    url = f"https://www.tradeindia.com/search.html?keyword=shampoo"
    response = requests.get(url)
    print(response)
        
    
query = input("Enter the product name: ")
getAmazonProducts(query)