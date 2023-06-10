import subprocess

tokenName = "TokenName"
tokenSymbol = "TokenSymbol"
tokenInitialSupply = 123
tokenInitialSupplyParameter = tokenInitialSupply * 1000000000

# Define the command you want to run
nftCommand = "npx locklift run -s ./scripts/1-deploy-sample.ts -n local"
tokenCommandLocal = f"npx locklift run -s ./scripts/1-deploy-token-root.ts \"{tokenName}\" \"{tokenSymbol}\" {tokenInitialSupplyParameter} -n local"
tokenCommandTestnet = "npx locklift run -s ./scripts/1-deploy-token-root.ts \"Testnet Python\" \"TP\" 100000000000 -n venom_testnet"

# Run the command and capture the output
output = subprocess.check_output(tokenCommandLocal, shell=True)

# Decode the output (assuming it's in UTF-8 encoding)
decoded_output = output.decode("utf-8")

# Print the output
print(decoded_output)
