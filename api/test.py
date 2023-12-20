import requests
from bs4 import BeautifulSoup

def get_exporters_products(query):
    url = f"https://www.tradeindia.com/search.html?keyword={query}"

    details_list = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tags = soup.find_all("div", class_='fullwidthcard')
        for script in script_tags:
            try:
                price_elem = script.find('p', class_='sc-51f6a3c3-12 dMowIp Body3R')
                price = price_elem.text.strip() if price_elem else "No Price"

                title_elem = script.find('h2', class_='sc-51f6a3c3-11 ipJJEc mb-1 card_title Body3R')
                title = title_elem.text.strip().split(',')[0] if title_elem else "No Title"

                image_elem = script.find('img', alt=True)
                image_url = image_elem['src'] if image_elem else "No Image URL"

                product_url_elem = script.find('a', href=True)
                product_url = product_url_elem['href'] if product_url_elem else "No Product URL"

                data = {"title": title, "price": price, "image_url": image_url, "product_url": product_url}
                details_list.append(data)
            except Exception as e:
                print(f"Error: {e}")
    else:
        print("Failed to fetch content from the URL")

    for data in details_list:
        for key, value in data.items():
            print(key, ":", value)
        print("\n")

query = input("Enter product name: ")
get_exporters_products(query)