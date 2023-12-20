import pandas as pd
import requests
payload={
    'source': 'google_shopping_search',
    'domain': 'com',
    'query': 'levis',
    'pages': 1,
    'context': [
        {' key': 'sort_by', 'value': 'pd'}, 
         {'key': 'min_price', 'value' :30},
    ],
    'parse': 'true',


}
response = requests. request (
'POST',
'https://realtime.oxylabs.io/v1/queries',
auth=( 'singh_chandanbir', 'Chandanbir1234'), 
json=payload
)
result=response.json()['results'][0]['contents']

products=result['results']['organic']

df=pd.DataFrame(columns=['Product Title', 'Price', 'Store'])

for p in products:
    title = p['title']
    price = p['price_str']
    store = p ['merchant '] ['name' ]

    df = pd.concat([pd.DataFrame([[title, price,store]], columns=df.columns), df], ignore_index=True)

df. to_csv('google_shopping_search.csv',index=False)
