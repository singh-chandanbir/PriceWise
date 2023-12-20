import re
import requests
from bs4 import BeautifulSoup

def getFlipkartProducts(url):
    
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
            price_element = product.find('div', class_='_30jeq3')
            if price_element:
                text_with_price = price_element.text  # Get the text content of the element
                numbers_only = re.findall(r'\d+', text_with_price)  # Extract integers using regex

                concatenated_string = ''.join(numbers_only)  # Concatenate numbers into a single string
                price = int(concatenated_string)
            image_url = product.find('img', class_='_396cs4')['src']
            product_url = 'https://www.flipkart.com' + product.find('a', class_='_2rpwqI')['href']
            data = {"title": title, "price": price, "image_url": image_url, "product_url": product_url}
            details_list.append(data)    
            count += 1

        return details_list
    
print(getFlipkartProducts("https://www.flipkart.com/pexpo-24-hrs-hot-cold-isi-certified-electro-vacuum-insulated-water-bottle-500-ml-flask/p/itmbbca112682c51?pid=BOTG2XE6CJ5EF8MG&lid=LSTBOTG2XE6CJ5EF8MGJEMLSE&marketplace=FLIPKART&q=flask&store=upp%2F3t7&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_IAH4QSDcdY_-RsnjkkxTypGlKr47oRPGwqOLcGUcILH54HHuZEkpGrpH9MD-CrHDCMT98ISWuT4fyvNwNTLE5Q%3D%3D&ppt=sp&ppn=sp&ssid=vewwi5jmvk0000001703059354288&qH=319c3206a7f10c17"))