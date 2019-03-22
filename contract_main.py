import json
from dragonchain_sdk import dragonchain_client

client = dragonchain_client.Client("<DC_ID>", "<AUTH_KEY>", "AUTH_KEY_ID")


# Posting NodeJs contract
print(json.dumps(client.post_contract(
    txn_type='node_contract',
    image="<docker_username>/<contract_name>:<latest>",
    cmd='node',
    args=['-m', 'index'],
    execution_order='parallel'
)))

# Updating NodeJs contract
print(json.dumps(client.update_contract(
    txn_type='node_contract',
    image="<docker_username>/<contract_name>:<latest>",
    cmd='node',
    args=['-m', 'index'],
    execution_order='parallel'
)))

# --------------------------------------------------------------

# Posting Python contract:
print(json.dumps(client.post_contract(txn_type='c1',
                                      image="<docker_username>/<contract_name>:<latest>",
                                      cmd='python',
                                      args=['-m', 'index'],
                                      execution_order='serial',
                                      auth="< docker_auth_token_optional >"
                                      )))

# Update Python contract:
print(json.dumps(client.update_contract(
    contract_id="<contract_id>",
    image="<docker_username>/<contract_name>:<latest>",
    cmd='python',
    execution_order='parallel',
    args=['-m', 'index'],
)))

# --------------------------------------------------------------

# Posting Go contract:
print(json.dumps(client.post_contract(
    txn_type='go_contract',
    image="<docker_username>/<contract_name>:<latest>",
    cmd='./handler',
    args=[''],
    execution_order='parallel',
    auth="< docker_auth_token_optional >"
)))

# Update Go contract:
print(json.dumps(client.update_contract(
    contract_id="<contract_id>",
    image="<docker_username>/<contract_name>:<latest>",
    cmd='./handler',
    execution_order='parallel',
    args=[''],
)))

# --------------------------------------------------------------

# Posting C++ contract:
print(json.dumps(client.post_contract(
    txn_type='csharp_contract',
    image="<docker_username>/<contract_name>:<latest>",
    cmd='./main',
    args=[''],
    execution_order='parallel',
    auth="< docker_auth_token_optional >"
)))

# Update C++ contract:
print(json.dumps(client.update_contract(
    contract_id="<contract_id>",
    image="<docker_username>/<contract_name>:<latest>",
    cmd='./main',
    execution_order='parallel',
    args=[''],
)))

# --------------------------------------------------------------

# Posting C# contract:
print(json.dumps(client.post_contract(
    txn_type='csharp_contract',
    image="<docker_username>/<contract_name>:<latest>",
    cmd='mono',
    args=['-m', 'Program'],
    execution_order='parallel',
    auth="< docker_auth_token_optional >"
)))

# Update C# contract:
print(json.dumps(client.update_contract(
    contract_id="<contract_id>",
    image="<docker_username>/<contract_name>:<latest>",
    cmd='mono',
    execution_order='parallel',
    args=['-m', 'Program'],
)))
