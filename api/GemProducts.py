import requests
from bs4 import BeautifulSoup as BS

def get_product_details(product):
    details_dict = {}
    title = product.find('span', class_='variant-title')
    
    if title:
        details_dict['product_title'] = title.text.strip()
        details_dict['product_brand'] = product.find('div', class_='variant-brand').text.replace('Brand:', '') if product.find('div', class_='variant-brand') else ''
        details_dict['product_min_qty'] = product.find('div', class_='variant-moq').text.replace('Min. Qty. Per Consignee:', '') if product.find('div', class_='variant-moq') else ''
        details_dict['product_list_price'] = product.find('span', class_='variant-final-price').text if product.find('span', class_='variant-final-price') else ''
        details_dict['product_final_price'] = product.find('span', class_='variant-list-price').text if product.find('span', class_='variant-list-price') else ''
        image_link = product.find('span', class_='responsive').find('img')['src']
        details_dict['product_image_link'] = image_link
        product_link = product.find('a', href=True)['href']
        details_dict['product_link'] = f"https://mkp.gem.gov.in{product_link}"
        return details_dict
    
    return None

def process_page(link):
    url = f"https://mkp.gem.gov.in{link}"
    response = requests.get(url)
    html_soup = BS(response.text, 'html.parser')
    
    product_detail_list = []
    product_list = html_soup.find_all('li', class_="clearfix")
    for product in product_list:
        details_dict = get_product_details(product)
        if details_dict is not None:
            product_detail_list.append(details_dict)
    return product_detail_list
