import re
import requests
from bs4 import BeautifulSoup

def getFlipkartProducts(query):
    url = f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    
    response = requests.get(url)
    
    details_list = []
    
    if response.status_code == 200:
        htmlsoup = BeautifulSoup(response.text, 'html.parser')
        products = htmlsoup.find_all("div", class_="_4ddWXP")
        
        count = 0
        
        for product in products:
            if count == 5:
                break
            
            title = product.find('a', class_='s1Q9rs').text
            price_element = product.find('div', class_='_30jeq3')
            if price_element:
                text_with_price = price_element.text  # Get the text content of the element
                price = re.findall(r'\d+\.*\d*', text_with_price)
            image_url = product.find('img', class_='_396cs4')['src']
            product_url = 'https://www.flipkart.com' + product.find('a', class_='_2rpwqI')['href']
            data = {"title": title, "price": price, "image_url": image_url, "product_url": product_url}
            details_list.append(data)    
            count += 1

        return details_list
    