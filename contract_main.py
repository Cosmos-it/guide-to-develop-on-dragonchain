import json
import dragonchain_sdk

client = dragonchain_sdk.Client('<DC_ID>', '<AUTH_KEY>''AUTH_KEY_ID')

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

# --------------------------------------------------------------

# Posting Python contract:
print(json.dumps(client.post_contract(
    txn_type='python_contract',
    image='image_name',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update Python contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='image_name',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting Go contract:
print(json.dumps(client.post_contract(
    txn_type='go_contract',
    image='image_name',
    cmd='./main',
    args=[''],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update Go contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='',
    cmd='./main',
    execution_order='parallel',
    args=[''],
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting C++ contract:
print(json.dumps(client.post_contract(
    txn_type='cpp_contract',
    image='image_name',
    cmd='./main',
    args=[''],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update C++ contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='image_name',
    cmd='./main',
    execution_order='parallel',
    args=[''],
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting C contract:
print(json.dumps(client.post_contract(
    txn_type='csharp_contract',
    image='image_name',
    cmd='./main',
    args=[''],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update C contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='image_name',
    cmd='./main',
    execution_order='parallel',
    args=[''],
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting C# contract:
print(json.dumps(client.post_contract(
    txn_type='csharp_contract',
    image='image_name',
    cmd='dotnet',
    args=['root.dll'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update C# contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='image_name',
    cmd='dotnet',
    args=['root.dll'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting Shell contract:
print(json.dumps(client.post_contract(
    txn_type='shell_contract',
    image='image_name',
    cmd='sh',
    args=['contract.sh'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update Shell contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='image_name',
    cmd='sh',
    args=['contract.sh'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))


# --------------------------------------------------------

# Delete a Smart Contract
print(json.dumps(client.delete_contract('<contract_id>')))