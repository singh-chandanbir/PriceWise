import requests
from bs4 import BeautifulSoup as BS

def getPages(search_query):

    search_query.replace(" ", "%20")

    url = "https://mkp.gem.gov.in/search?q="+search_query

    response = requests.get(url)
    
    if response.status_code == 200:
        htmlcontent = response.text
        htmlsoup = BS(htmlcontent, 'html.parser') 
        result_dict = {}
        categories = htmlsoup.find_all('li', class_='bn-group')
        for category in categories:
            category_name = category.find('strong').text.strip()
            links = category.find_all('li', class_='bn-link')
            
            category_dict = {}
            for link in links:
                link_text = link.text.strip()
                href = link.a['href']
                category_dict[link_text] = href
                result_dict[category_name] = category_dict

    return (result_dict)
    