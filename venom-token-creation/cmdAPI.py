import subprocess

# Define the command you want to run
nftCommand = "npx locklift run -s ./scripts/1-deploy-sample.ts -n local"
tokenCommand = "npx locklift run -s ./scripts/1-deploy-token-root.ts \"VenomChat Token\" \"VCHAT\" 100000000000 -n local"

# Run the command and capture the output
output = subprocess.check_output(tokenCommand, shell=True)

# Decode the output (assuming it's in UTF-8 encoding)
decoded_output = output.decode("utf-8")

# Print the output
print(decoded_output)
