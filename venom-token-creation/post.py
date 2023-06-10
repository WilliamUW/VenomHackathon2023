import requests

# API endpoint URL
# url = 'https://8d2d-184-147-53-58.ngrok-free.app/tokens?tokenName=Name&tokenSymbol=Symbol&tokenInitialSupply=123'
url = 'https://8d2d-184-147-53-58.ngrok-free.app/nfts?nftName=Name&nftDescription=Symbol&nftImageUrl=google.com&nftSourceUrl=google.com'

# Send POST request
response = requests.post(url)

# Print the response
print(response.json())
