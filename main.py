import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

# Load your SerpApi API key from environment variables
load_dotenv()
api_key = os.getenv('031e45f49f7c79e208bcfe7d26d871e0e1485459c1a3946ffe4e1b88e970251a')

# Set the search parameters
params = {
    'engine': 'google_shopping',
    'q': 'your query',  # Replace with your desired search query
}

# Make the API request
search = client.search(params)
search.params['api_key'] = api_key  # Set the API key separately in the params dictionary
results = search.get_dict()

# Extract and print the relevant data from the results
for product in results.get('shopping_results', []):
    print(f"Product: {product.get('title')}")
    print(f"Price: {product.get('price')}")
    print(f"URL: {product.get('link')}")
    print("------")
