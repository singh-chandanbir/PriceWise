import requests
from bs4 import BeautifulSoup

def get_exporters_products(query):
    url = f"https://www.exportersindia.com/search.php?srch_catg_ty=prod&term={query}&cont=IN&ss_status=N"

    # Fetch the HTML content from the URL
    details_list = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all <script> tags
        script_tags = soup.find_all("div", class_='class_box_sec')
        # Iterate through each script tag to find the desired data
        for script in script_tags:
            price = script.find('span', class_='black fw6 large').text if script.find('span', class_='black fw6 large') else "Contact"
            if price != "Contact":
                title = script.find('a', class_='prdclk').text if script.find('a', class_='prdclk') else "No Title"
                brand = script.find('a', class_='blue fw6 com_nam').text if script.find('a', class_='blue fw6 com_nam') else "No Brand"
                image_elem = script.find('img', class_='utmlazy')
                image_url = image_elem['src'] if image_elem else "No Image URL"
                product_url_elem = script.find('a', class_='prdclk')
                product_url = product_url_elem['href'] if product_url_elem else "No Product URL"
                data = {"title": title, "price": price, "brand": brand, "image": image_url, "product_link": product_url}
                details_list.append(data)    
        
        return details_list
        
    else:
        print("Failed to fetch content from the URL")

query = input("Enter product name: ")
list = get_exporters_products(query)

for product in list:
    for key, value in product.items():
        print(key, " : ", value)