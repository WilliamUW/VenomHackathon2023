from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/tokens', methods=['POST'])
def create_token():
    # Retrieve parameters from the request body
    tokenName = request.json.get('tokenName')
    tokenSymbol = request.json.get('tokenSymbol')
    tokenInitialSupply = request.json.get('tokenInitialSupply')
    tokenInitialSupplyParameter = tokenInitialSupply * 1000000000

    tokenCommandLocal = f"npx locklift run -s ./scripts/1-deploy-token-root.ts \"{tokenName}\" \"{tokenSymbol}\" {tokenInitialSupplyParameter} -n local"

    # Run the command and capture the output
    output = subprocess.check_output(tokenCommandLocal, shell=True)

    # Decode the output (assuming it's in UTF-8 encoding)
    decoded_output = output.decode("utf-8")

    # Print the output
    print(decoded_output)

    subtext = "deployed at: "

    before, _, after = decoded_output.partition(subtext)
    after = after.replace('\n', '')

    # Example response with created token details
    token = {
        'name': tokenName,
        'symbol': tokenSymbol,
        'initialSupply': tokenInitialSupply,
        'id': after,
    }

    return jsonify(token), 201

if __name__ == '__main__':
    app.run()
