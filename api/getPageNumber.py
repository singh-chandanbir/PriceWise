import requests
from bs4 import BeautifulSoup

def get_page_number(url):
    content = requests.get(url)
    htmlsoup = BeautifulSoup(content.text, 'html.parser')
    
    if htmlsoup.find('div', id='no-results-found'):
        return None
    
    highest_page_number=1
    
    if (htmlsoup.find('div', class_="pagination")):
        detailsDict = {}
        page_links = htmlsoup.select('div.pagination a')
        page_numbers = [int(link['href'].split('=')[-1]) for link in page_links]
        highest_page_number = max(page_numbers)
        
    return highest_page_number
    