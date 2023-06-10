import requests

# API endpoint URL
url = 'http://localhost:5000/tokens'

# Request body data
data = {
    'tokenName': 'New Book',
    'tokenSymbol': 'John Doe',
    'tokenInitialSupply': 69
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
print(response.json())
