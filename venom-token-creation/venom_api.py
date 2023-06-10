from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

import re

def extract_text_between_subtexts(text, start_subtext, end_subtext):
    pattern = re.escape(start_subtext) + r'(.*?)' + re.escape(end_subtext)
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return ""


@app.route('/tokens', methods=['POST'])
def create_token():
    # Retrieve parameters from the request body
    tokenName = request.args.get('tokenName')
    tokenSymbol = request.args.get('tokenSymbol')
    tokenInitialSupply = request.args.get('tokenInitialSupply')
    tokenInitialSupplyParameter = int(tokenInitialSupply) * 1000000000

    print(tokenName)
    print(tokenSymbol)
    print(tokenInitialSupply)


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

    everBalance = extract_text_between_subtexts(decoded_output, "the giver balance is: ", " ever")

    # Example response with created token details
    token = {
        'name': tokenName,
        'symbol': tokenSymbol,
        'initialSupply': tokenInitialSupply,
        'everBalance': everBalance,
        'id': after,
    }

    return jsonify(token), 201

if __name__ == '__main__':
    app.run()
