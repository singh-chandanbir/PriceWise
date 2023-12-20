import requests

url = "https://www.amazon.in/s?"

response = requests.get(url)

print(response.status_code)