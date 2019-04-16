# Welcome to Dragonchain

## Guide to building on Dragonchain

### Overview

* [Audience](#audience)
* [Design](#design)
* [Basic Requirements](#basic-requirements)
* [Smart Contract](#smart-contract)
  * [Dragonchain Smart Contract](#dragonchain-smart-contract)
  * [Deploy a Smart Contract](#deploy-a-smart-contract)
  * [Update a Smart Contract](#update-a-smart-contract)
  * [Delete a Smart Contract](#delete-a-smart-contract)
* [Transaction](#transaction)
  * [Register a Transaction](#register-a-transaction)
  * [Post a Transaction](#post-a-transaction)
  * [Update a Transaction](#register-a-transaction)
  * [Query a Transaction](#query-a-transaction)

### Audience

This document is for developers and enterprises who are:

* Interested in Dragonchain Platform
* Looking to write Smart Contracts

### Design

* Flexibility: Developers can create smart contracts as docker containers with the ability to update and delete after deployment.
The Dragonchain platform
* Simplicity: Dragonchain has SDKs in Python and Nodejs to help users interact with their chains.

### Basic Requirements

* Must have a Dragonchain Console account
* Must download Dragonchain SDK of your choice: [Python](https://github.com/dragonchain-inc/dragonchain-sdk-python) or [Node.js](https://github.com/dragonchain-inc/dragonchain-sdk-node) SDK
* Must know how to push docker image to Docker registry

### Smart Contract

Smart contracts facilitate credible transactions in a verifiable and permanent manner, without the need for third parties.

#### Dragonchain Smart Contract

[Access Smart Contract Templates](https://github.com/dragonchain-inc/guide-to-develop-on-dragonchain/tree/master/smart-contract-templates)

#### Deploy a Smart Contract

Clone the Smart Contract template and choose python_contract

```sh
git clone https://github.com/dragonchain-inc/guide-to-develop-on-dragonchain
cd guide-to-develop-on-dragonchain
cd python_contract
```

If you are not using docker hub, the steps below might look different. We will now build and push a Smart Contract docker image to Dragonchain.

```sh
docker build -t  taban/python_contract .
docker push taban/python_contract:latest
```

After pushing the Smart Contract to a docker registry, we will use the [Python SDK](https://python-sdk-docs.dragonchain.com/latest/) to deploy our Smart Contract.

```sh
pip install dragonchain-sdk
```

We will create a file called index.py and incrementally add code.

```python
import json
import dragonchain_sdk
client = dragonchain_sdk.Client('<DC_ID>', '<AUTH_KEY>', 'AUTH_KEY_ID')

# Post Smart Contract
print(json.dumps(dragonchain_client.post_contract(
    txn_type='example_contract',
    image='taban/python_contract',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
    # auth='<docker_auth_token_if_private_repository>'
)))
```

Response from Dragonchain

```json
{
    "ok": true,
    "response": {
        "success": {
            "args": [
                "index"
            ],
            "auth_key_id": null,
            "cmd": "paython",
            "cron": null,
            "dcrn": "SmartContract::L1::AtRest",
            "env": null,
            "execution_order": "parallel",
            "existing_secrets": null,
            "id": "2cb7589b-1218-42b7-b876-7a05392d86c9",
            "image": "taban/python_contract:latest",
            "image_digest": null,
            "seconds": null,
            "status": {
                "msg": "Contract creating",
                "state": "Pending",
                "timestamp": "2019-04-05 22:59:52.653891"
            },
            "txn_type": "example_contract",
            "version": "3"
        }
    },
    "status": 202
}
```

#### Update a Smart Contract

```python

# Update Smart Contract
print(json.dumps(dragonchain_client.update_contract(
    contract_id='<contract_id>',
    image='taban/python_contract:latest',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
    # auth='<docker_auth_token_if_private_repository>'
)))
```

Response from Dragonchain

```json
{
    "ok": true,
    "response": {
        "success": {
            "args": [
                "index"
            ],
            "auth_key_id": null,
            "cmd": "paython",
            "cron": null,
            "dcrn": "SmartContract::L1::AtRest",
            "env": {},
            "execution_order": "parallel",
            "existing_secrets": [],
            "id": "2cb7589b-1218-42b7-b876-7a05392d86c9",
            "image": "taban/python_contract:latest",
            "image_digest": null,
            "seconds": null,
            "status": {
                "msg": "",
                "state": "updating",
                "timestamp": "2019-04-05 23:06:35.334432"
            },
            "txn_type": "example_contract",
            "version": "1"
        }
    },
    "status": 202
}

```

#### Delete a Smart Contract

```python
# Delete a Smart Contract
print(json.dumps(dragonchain_client.delete_contract('<contract_id>')))
```

```json
{
    "ok": true,
    "response": {
        "success": {
            "args": [
                "index"
            ],
            "auth_key_id": null,
            "cmd": "paython",
            "cron": null,
            "dcrn": "SmartContract::L1::AtRest",
            "env": {},
            "execution_order": "parallel",
            "existing_secrets": [],
            "id": "2cb7589b-1218-42b7-b876-7a05392d86c9",
            "image": "taban/python_contract:latest",
            "image_digest": null,
            "seconds": null,
            "status": {
                "msg": "",
                "state": "deleting",
                "timestamp": "2019-04-08 16:28:03.427830"
            },
            "txn_type": "example_contract",
            "version": "1"
        }
    },
    "status": 202
}
```

### Transaction

#### Register a transaction type

```python
print(json.dumps(dragonchain_client.register_transaction_type('currency')))
```

#### Post a transaction

Posting a transaction to currency transaction

```python
# Currency contract
print(json.dumps(dragonchain_client.post_transaction('currency', {
    'version': '1',
    'paymentData': {
        'amount': 500,
        'to': 'John Howies',
        'type': 'dining'
    }
})))
```

Response from Dragonchain

```json
{
    "ok": true,
    "response": {
        "transaction_id": "5b64cd77-6d7e-48ba-8004-5c276ed43da7"
    },
    "status": 201
}
```

Post a transaction to our python_contract under the txn_type='example_contract'

```python
print(json.dumps(dragonchain_client.post_transaction('example_contract', {
    'version': '1',
    'exampleData': {
        'type': 'test',
'message': 'Hello, world!'
    }
})))
```

Response from Dragonchain

Save the transaction_id returned by your example

```json
{
    "ok": true,
    "response": {
        "transaction_id": "98f1c816-48d0-4db6-94e5-10d175d4d145"
    },
    "status": 201
}
```

#### Update a Transaction

```python
print(json.dumps(dragonchain_client.register_transaction_type('currency')))
```

#### Query a Transaction

Query currency transaction

Grab the transaction id returned by currency

```python
# # Query currency
print(json.dumps(dragonchain_client.query_transactions(query='txn_id:"5b64cd77-6d7e-48ba-8004-5c276ed43da7"')))
```

Response from Dragonchain

```json
{
    "ok": true,
    "response": {
        "results": [
            {
                "dcrn": "Transaction::L1::FullTransaction",
                "header": {
                    "block_id": "24453725",
                    "dc_id": "9cf00a35-ccb1-4f0b-a3d5-d63237b9139d",
                    "invoker": "",
                    "tag": "",
                    "timestamp": "1554506841",
                    "txn_id": "5b64cd77-6d7e-48ba-8004-5c276ed43da7",
                    "txn_type": "currency"
                },
                "payload": {
                    "paymentData": {
                        "amount": 500,
                        "to": "John Howies",
                        "type": "dining"
                    },
                    "version": "1"
                },
                "proof": {
                    "full": "JB6VLlxFTkvcCOe2sGNy44lVl0Qaas4Q8FUl8fjvf6E=",
                    "stripped": "MEUCIQDncsLMgjawR1oOovBLHI0zPgYkCxuC2gjNDIV6smJ2VAIgHMfXV/jYfaGoeqrdMGmCv+o74lCFVO3jcAKZ18QztDw="
                },
                "version": "1"
            }
        ],
        "total": 1
    },
    "status": 200
}
```

Query example_contract transaction

Grab the transaction id returned by example_contract

```python
# Query example_contract
print(json.dumps(dragonchain_client.query_transactions('txn_id:"02c3652e-e5ae-425b-9413-986d9b844cb6"')))
```

Response from Dragonchain

```json
{
    "ok": true,
    "response": {
        "results": [
            {
                "dcrn": "Transaction::L1::FullTransaction",
                "header": {
                    "block_id": "24453533",
                    "dc_id": "9cf00a35-ccb1-4f0b-a3d5-d63237b9139d",
                    "invoker": "",
                    "tag": "",
                    "timestamp": "1554505884",
                    "txn_id": "98f1c816-48d0-4db6-94e5-10d175d4d145",
                    "txn_type": "example_contract"
                },
                "payload": {
                    "exampleData": {
"message": "Hello, world!",
                        "type": "test"
                    },
                    "version": "1"
                },
                "proof": {
                    "full": "A0u2d3f6JROLZcGeZaX0ijOJfe16VYJ5bA7IP4XrT+k=",
                    "stripped": "MEUCIQCY0+dh706AqhOYS1hr9CMk7xxP9IBQG8743PP0C2TZNgIgXkQyBO1XmQBWRNlwaQ8vp0EwddAPTBxpmViXlmi6iY4="
                },
                "version": "1"
            }
        ],
        "total": 1
    },
    "status": 200
}
```

Note:
> Our system also allows developers to add scheduled smart contract execution using a cron expression or seconds between broadcasts. For example, `cron=’* * * * *’` and `seconds=59` are both valid. These fields are optional. If you are going to use a scheduler, you can only use a cron or seconds, not both.

### Contribute SDK

Currently, Dragonchain supports two SDKs ([Python](https://github.com/dragonchain-inc/dragonchain-sdk-python) and [Node.js](https://github.com/dragonchain-inc/dragonchain-sdk-node)) internally, but we would like to have many SDK options to reflect our system capabilities. If you have any questions or concerns, please join our community developer forum on Telegram (Community Dragonchain Dev Official).
