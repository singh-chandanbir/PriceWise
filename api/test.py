import requests
from bs4 import BeautifulSoup

def getFlipkartProducts(query):
    url = f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    
    response = requests.get(url)
    
    details_list = []
    
    if response.status_code == 200:
        htmlsoup = BeautifulSoup(response.text, 'html.parser')
        products = htmlsoup.find_all("div", class_="_4ddWXP")
        for product in products:
            title = product.find('a', class_='s1Q9rs').text
            price = product.find('div', class_='_30jeq3').text
            image_url = product.find('img', class_='_396cs4')['src']
            product_url = product.find('a', class_='s1Q9rs')['href']
            data = {"title": title, "price": price, "image_url": image_url, "product_url": product_url}
            details_list.append(data)        

        for data in details_list:
            for key, value in data.items():
                print(key, " : ", value)
            print("\n")
    
    
getFlipkartProducts(input("Enter your query: "))