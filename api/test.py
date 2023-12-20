import requests
from bs4 import BeautifulSoup

url = "https://mkp.gem.gov.in/purses-and-handbags-and-bags-office-bags-and-laptop-bags/search#/?q=bags"

html = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(html.text, 'html.parser')

page_title = soup.title.string.strip()
first_part = page_title.split('|')[0].strip()

print("{",first_part,"}")