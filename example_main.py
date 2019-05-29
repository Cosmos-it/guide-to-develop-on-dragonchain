import json
import dragonchain_sdk

client = dragonchain_sdk.Client(dragonchain_id='your_dc_id', auth_key_id='your_auth_id', auth_key='your_auth_key', endpoint='https://your_dc_id.api.dragonchain.com')


# Posting NodeJs contract
print(json.dumps(client.create_smart_contract(
    transaction_type='contract_name',
    image='image_name',
    cmd='node',
    args=['index.js'],
    execution_order='parallel',
    # registry_credentials='<docker_auth_token_if_private_repository>'
)))


# Updating NodeJs contract
# print(json.dumps(client.update_contract(
#     contract_id='<contract_id>',
#     image='your_contract_image_name',
#     cmd='node', 
#     args=['index.js'],
#     execution_order='parallel',
#     auth='<docker_auth_token_if_private_repository>'
# )))

# To post smart contract written in different languages, 
# change the cmd and args values.

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
# print(client.delete_contract('<contract_id>'))
