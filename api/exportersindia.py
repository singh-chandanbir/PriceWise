import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_exporters_products(query):
    url = f"https://www.exportersindia.com/search.php?srch_catg_ty=prod&term={query}&cont=IN&ss_status=N"

    # Fetch the HTML content from the URL
    details_list = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tags = soup.find_all("div", class_='class_box_sec')
        for script in script_tags:
            price = script.find('span', class_='black fw6 large').text if script.find('span', class_='black fw6 large') else "Contact"
            if price != "Contact":
                title = script.find('a', class_='prdclk').text if script.find('a', class_='prdclk') else "No Title"
                search_index = title.find(",")
                if search_index != -1:
                    title = title[: search_index]
                brand = script.find('a', class_='blue fw6 com_nam').text if script.find('a', class_='blue fw6 com_nam') else "No Brand"
                image_elem = script.find('img', class_='utmlazy')
                image_url = image_elem['src'] if image_elem else "No Image URL"
                product_url_elem = script.find('a', class_='prdclk')
                product_url = product_url_elem['href'] if product_url_elem else "No Product URL"
                data = {"title": title, "brand": brand, "price": price, "image_url": image_url, "product_url": product_url}
                details_list.append(data)        
    else:
        print("Failed to fetch content from the URL")

    for data in details_list:
        for key, value in data.items():
            print(key, " : ", value)
        print("\n")
        
query = input("Enter product name: ")
get_exporters_products(query)