import json
import dragonchain_sdk

client = dragonchain_sdk.Client(dragonchain_id='your_dc_id', auth_key_id='your_auth_key_id', auth_key='your_auth_key')

# Posting NodeJs contract
print(json.dumps(client.post_contract(
    txn_type='node_contract',
    image='image_name',
    cmd='node',
    args=['index.js'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Updating NodeJs contract
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='image_name',
    cmd='node', 
    args=['index.js'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# To post smart contract written in different languages, 
# the cm and args values.

# -----------------------
# Python commands:
# cmd='python',
# args=['-m', 'index'],

# -----------------------
# Posting Go contract:
# cmd='./main',
# args=[''],

# ------------------------
# Posting C/C++ contract:
# cmd='./main'
# args=['']

# -----------------------
# Posting C# contract:
# cmd='dotnet',
# args=['root.dll'],

# ------------------------
# Posting Shell contract:
# cmd='sh',
# args=['contract.sh'],

# --------------------------------------------------------
# Delete a Smart Contract
# print()client.delete_contract('<contract_id>'))