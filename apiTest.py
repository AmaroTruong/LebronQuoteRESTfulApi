import json

# Base URL of the Flask API
base_url = 'http://localhost:5000'

# Set the Content-Type header to application/json
headers = {'Content-Type': 'application/json'}

# Retrieve all quotes (GET request)
response = requests.get(f'{base_url}/quotes')
print('GET All Quotes:')
print(response.json())
print('')

# Retrieve a specific quote (GET request)
quote_id = 'quote1'
response = requests.get(f'{base_url}/quotes/{quote_id}')
print(f'GET Quote {quote_id}:')
print(response.json())
print('')

# Create a new quote (POST request)
data = {'quote': 'New quote content'}
response = requests.post(f'{base_url}/quotes', json=data, headers=headers)
print('POST New Quote:')
print(response.json())
print('')

# Update an existing quote (PUT request)
quote_id = 'quote1'
data = {'quote': 'Updated quote content'}
response = requests.put(f'{base_url}/quotes/{quote_id}', json=data, headers=headers)
print(f'PUT Updated Quote {quote_id}:')
print(response.json())
print('')

# Delete a quote (DELETE request)
quote_id = 'quote2'
response = requests.delete(f'{base_url}/quotes/{quote_id}')
print(f'DELETE Quote {quote_id}:')
print(response.status_code)
print('')

# Retrieve all quotes after modifications (GET request)
response = requests.get(f'{base_url}/quotes')
print('GET All Quotes after Modifications:')
print(response.json())
