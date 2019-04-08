# Welcome to Dragonchain

## Guide to building on Dragonchain

### Overview

* Audience
* Design goals
* Basic Requirements
* Smart Contract
  * Dragonchain Smart Contract
  * Deploying a Smart Contract
  * Updating a Smart Contract
  * Deleting a Smart Contract
* Transaction
  * Register a transaction
  * Register a transaction
  * Update a transaction
  * Query a transaction

### Audience

This document is for developers and enterprises who are:

* Interested in Dragonchain Platform
* Looking to write Smart Contracts

### Design Goals

Why would you choose Dragonchain platform over other blockchain solutions?

* Flexibility: Developers can create smart contracts as docker containers with the ability to update and delete after deployment.
* Scalability:  Dragonchain platform doesn’t use algorithm such as PoW or PoS. Instead we use public blockchains for pinning without running our own.
* Simplicity: Dragonchain has rolled out an in house SDKs in Python and python.js to help developers interact with Dragonchain platform easily

### Basic Requirements

* Must have a Dragonchain Console account (Keys)
* Download our Dragonchain SDK of your choice [Link to python and Python SDK]
* Must know how to push docker image to Docker registry

### Smart Contract

Smart contract facilitate credible transactions in a traceable and permanent manner, without the need for third parties. Smart contract allow users to control which contractual clauses are made partially or entirely self-executing and self-enforcing.

#### *Dragonchain Smart Contract*

Creating a Smart Contract on Dragonchain is very straightforward. Take a look at our templates to get an idea of what languages you might be interested in getting started with. If you want to develop your own Smart Contract in a different language, you can use our template as a guide.

#### *Deploying a Smart Contract*

For a simple example, we will deploy a Python Smart Contract from our existing templates.

Clone the Smart Contract template and choose the python_contract

```bash
$ clone https://github.com/dragonchain-inc/guide-to-develop-on-dragonchain
$ cd guide-to-develop-on-dragonchain
$ cd python_contract
```

If you are not using docker hub, the steps below might look different. We will now build and push a Smart Contract docker image to Dragonchain.

```bash
$ docker build -t  taban/python_contract .
$ docker push taban/python_contract:latest
```

After pushing the Smart Contract to a docker registry, we will then use Python SDK to deploy our Smart Contract. Go to this link to download the [Python SDK](https://python-sdk-docs.dragonchain.com/latest/)

```bash
$ pip install dragonchain-sdk
```

Lets create a file called index.py. We will incrementatlly add code to this file you created until the end.

```python
import json
import dragonchain_sdk

dragonchain_client = dragonchain_sdk.client(dragonchain_id='your_dc_id')  
dragonchain_client.override_credentials('auth_key', 'auth_key_id')
```

Note:
> Our system also allows developers to add scheduled smart contract execution using cron/seconds. Example: ```cron=’* * * * *’/seconds=60``` This is optional. If you are going to use a scheduler, remember that you can only use a cron or seconds but NOT both.

Using Python SDK [Share code and video]

```py
# Post Smart Contract
print(json.dumps(dragonchain_client.post_contract(
    txn_type='example_contract',
    image='taban/python_contract',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
    # auth='<docker_auth_token_if_private_repository>'
)), indent=4, sort_keys=True)
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

#### *Updating a Smart Contract*

With the ability to update deployed Smart Contracts, businesses are not tied to building immutable Smart Contracts that are costly. Instead, handling of Smart Contract was architected to simulate a true software life-cycle. You will always be sure that the right version of your Smart Contract is deployed to Dragonchain and that it achieves its goals.

```py

# Update Smart Contract
print(json.dumps(dragonchain_client.update_contract(
    contract_id='<contract_id>',
    image='taban/python_contract:latest',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
    # auth='<docker_auth_token_if_private_repository>'
), indent=4, sort_keys=True))
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

#### *Deleting a Smart Contract*

Dragonchain platform allows for deletion of Smart Contract which you may no longer want to use. This is also a huge win for businesses/developers since they get to have control over what they deploy on Dragonchain.

Example: [Provide code example and video demo]

```py
# Delete a Smart Contract
print(json.dumps(dragonchain_client.delete_contract('<contract_id>'), =4, sort_keys=True))
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

Unlike other platforms out there, Dragonchain platform allows you to register a transaction and start using it without developing a Smart Contract. As business/developer, your architecture will handle posting, updating and retrieving of transactions.

You might ask how does posting a transaction to a Smart Contract work?
It is similar to posting a transaction to a registered transaction. However, when a Smart Contract is created on Dragonchain, the system will create two transactions, one with invoker and another without.

#### *Register a transaction*

```py
print(json.dumps(dragonchain_client.register_transaction_type('currency', ''), indent=4, sort_keys=True))
```

#### *Post a transaction*

Posting a transaction to currency transaction

```py
# Currency contract
print(json.dumps(dragonchain_client.post_transaction('currency', {
    'version': '1',
    'paymentData': {
        'amount': 500,
        'to': 'John Howies',
        'type': 'dining'
    }
}), indent=4, sort_keys=True))
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

```py
print(json.dumps(dragonchain_client.post_transaction('example_contract', {
    'version': '1',
    'exampleData': {
        'type': 'test',
        'message': 'Hellow, world!'
    }
}), indent=4, sort_keys=True))
```

Response from Dragonchain

> Save the transaction_id returned by your example

```json
{
    "ok": true,
    "response": {
        "transaction_id": "98f1c816-48d0-4db6-94e5-10d175d4d145" 
    },
    "status": 201
}
```


#### *Update a Transaction*

Dragonchain allows you to update transaction custom indexes only. The custom indexes will allow you query transaction easily.

```py
print(json.dumps(dragonchain_client.register_transaction_type('currency', ''), indent=4, sort_keys=True))
```

#### *Query a Transaction*

Query currency transaction

Grab the transaction id returned by currency

```py
# # Query currency
print(json.dumps(dragonchain_client.query_transactions(
    'txn_id:"5b64cd77-6d7e-48ba-8004-5c276ed43da7"'
), indent=4, sort_keys=True))
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


```py
# Query example_contract
print(json.dumps(dragonchain_client.query_transactions('txn_id:"02c3652e-e5ae-425b-9413-986d9b844cb6"'
), indent=4, sort_keys=True))
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
                        "message": "Hellow, world!",
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


### Contribute SDK

Currently, Dragonchain supports two SDKs (Python and python.js) internally, but we would like to have many SDK options to reflect our system capabilities. If you have any questions or concerns, please join our community developer forum on Telegram (Community Dragonchain Dev Official).
