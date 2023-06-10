import requests

# API endpoint URL
tokenUrl = 'https://8d2d-184-147-53-58.ngrok-free.app/tokens?tokenName=Name&tokenSymbol=Symbol&tokenInitialSupply=123'
nftUrl = 'https://8d2d-184-147-53-58.ngrok-free.app/nfts?nftName=Name&nftDescription=Symbol&nftImageUrl=google.com&nftSourceUrl=google.com'

# Send POST request
# response = requests.post(tokenUrl)
response = requests.post(nftUrl)

# Print the response
print(response.json())
