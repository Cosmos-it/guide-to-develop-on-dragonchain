import json
from dragonchain_sdk import dragonchain_client

client = dragonchain_client.Client('<DC_ID>', '<AUTH_KEY>', 'AUTH_KEY_ID')


# Posting NodeJs contract
print(json.dumps(client.post_contract(
    txn_type='node_contract',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='node',
    args=['index.js'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Updating NodeJs contract
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='node',
    args=['index.js'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting Python contract:
print(json.dumps(client.post_contract(
    txn_type='python_contract',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update Python contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting Go contract:
print(json.dumps(client.post_contract(
    txn_type='go_contract',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='./main',
    args=[''],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update Go contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='./main',
    execution_order='parallel',
    args=[''],
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting C++ contract:
print(json.dumps(client.post_contract(
    txn_type='cpp_contract',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='./main',
    args=[''],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update C++ contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='./main',
    execution_order='parallel',
    args=[''],
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting C contract:
print(json.dumps(client.post_contract(
    txn_type='csharp_contract',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='./main',
    args=[''],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update C contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='./main',
    execution_order='parallel',
    args=[''],
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting C# contract:
print(json.dumps(client.post_contract(
    txn_type='csharp_contract',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='dotnet',
    args=['root.dll'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update C# contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='dotnet',
    args=['root.dll'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# --------------------------------------------------------------

# Posting Shell contract:
print(json.dumps(client.post_contract(
    txn_type='shell_contract',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='sh',
    args=['contract.sh'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))

# Update Shell contract:
print(json.dumps(client.update_contract(
    contract_id='<contract_id>',
    image='<docker_username>/<contract_name>:<latest>',
    cmd='sh',
    args=['contract.sh'],
    execution_order='parallel',
    auth='<docker_auth_token_if_private_repository>'
)))
