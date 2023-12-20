import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

# Load your SerpApi API key from environment variables
load_dotenv()
api_key = os.getenv('SERPAPI_API_KEY')  # Update with your actual environment variable name

# Set the search parameters
params = {
    'engine': 'google_shopping',
    'q': 'your query',  # Replace with your desired search query
}

# Create an instance of GoogleSearch with your API key and search parameters
client = GoogleSearch({"api_key": api_key, "engine": "google_shopping", "q": params['q']})

# Make the API request
results = client.get_dict()

# Check if any results are received
if 'shopping_results' in results:
    # Extract and print the relevant data from the results
    for product in results['shopping_results']:
        print(f"Product: {product.get('title')}")
        print(f"Price: {product.get('price')}")
        print(f"URL: {product.get('link')}")
        print("------")
else:
    print("No shopping results found.")
