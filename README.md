# Welcome to Dragonchain

## Guide to building on Dragonchain

### Contents

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
* [Node example](#node-example)

### Audience

This document is for developers and enterprises who are:

* Interested in Hybrid Blockchains
* Looking to write Upgradeable Smart Contracts

### Design

* Flexibility: Developers can create smart contracts as docker containers with the ability to update and delete them even after deployment.
* Simplicity: Dragonchain has official SDKs in Python, NodeJS, Golang and a community SDK in C# helping users interact with their chains.

### Prerequisites

1) Register for a Dragonchain [Console account](https://account.dragonchain.com)
2) Download a Dragonchain SDK of your choice: [Python](https://github.com/dragonchain-inc/dragonchain-sdk-python) or [Node.js](https://github.com/dragonchain-inc/dragonchain-sdk-node) _(more coming soon...)_


### Smart Contract

#### Dragonchain Smart Contract

[Access Smart Contract Templates](https://github.com/dragonchain-inc/guide-to-develop-on-dragonchain/tree/master/smart-contract-templates)

#### Deploy a Smart Contract

1) Open up your Terminal/Bash Prompt and clone the smart contract template. Then change into the python_contract directory

```sh
$ git clone https://github.com/dragonchain-inc/guide-to-develop-on-dragonchain
$ cd guide-to-develop-on-dragonchain
$ cd smart-contract-templates
$ cd python_contract
```

2) Change to your home directory and create a python virtual environment as per best practice *(change dragonvenv to any suitable name)*

```sh
$ virtualenv -p python3 dragonvenv
```
3) Activate your virtual environment. (type in 'deactivate' when you want to leave the virtual environment later)*

```sh
 $ source dragonvenv/bin/activate
```

4) Install the [Python SDK](https://python-sdk-docs.dragonchain.com/latest/) to interface with your smart contract

```sh
 $ sudo pip3 install dragonchain-sdk
```
5) Open up your favourite web browser and register for a DockerHub Account: https://hub.docker.com/signup <br/> *(or login into your existing one)*

6) Click 'Create a Repository'
<br/><br/>
7) Enter a 'Name' for your repository, e.g. "interchain"
<br/><br/>
8) Now go back to your Terminal, and build your docker image from the Dockerfile in the /python_contract sub-directory

```sh
$ docker build -t  any_image_name .
```

9) Then push your smart contract image to your newly created docker registry <br/> *(substitute docker_id, repo_name, tag_name with your own values!)*

```sh
$ docker push docker_id/repo_name:tagname
```

*   *For example, in our case we might do: docker push 19011/interchain:stellar*

10) Go back to your web browser and log into your [Dragonchain Console account](https://account.dragonchain.com/login)
<br/><br/>

11) Go to the 'Create Chain' section and choose a name for your new hybrid chain, then click create. <br/> *(Leave Level as 'Level 1' )*
<br/><br/>
![alt text](https://joycoin.files.wordpress.com/2019/05/level1-chain.png?w=840)
<br/><br/>
12) Note down the Chain ID of your new chain and keep it secure! <br/> *(In our chain 'misty-silence', the Chain ID happends to be 'fcf62a0f-5904-428a-bc7d-99e974fa89e0')*
<br/><br/>
![alt text](https://joycoin.files.wordpress.com/2019/05/screenshot-from-2019-05-22-21-10-48.png?w=840)
<br/><br/>
13) Click 'View Chain' and navigate to the dashboard of your newly created hybrid chain. Scroll down to the 'MISC' section and click on 'Generate New API Key' on the bottom right.
<br/><br/>
![alt text](https://joycoin.files.wordpress.com/2019/05/screenshot-from-2019-05-22-21-43-36.png)
<br/><br/>
14) Note down the Auth Key ID and Auth Key and keep them secure! <br/> *(The 'Auth Key ID' in our case is 'NNIPQSWIKNYV' and the 'Auth Key' is 'MabBUglfjl87LVLZFJQCahxrKfEQojhc')*
<br/><br/>
![alt text](https://joycoin.files.wordpress.com/2019/05/screenshot-from-2019-05-22-21-15-01.png)



15) Now go back to the Terminal, and open up the file index.py with your favourite editor. Delete any existing lines of code.  <br/>  *(We use Atom here but you can use Sublime, VisualStudio, Vim or even EMACS if you really fancy.)*

```sh
atom index.py
```

16) Copy (Ctrl + C), paste (Ctrl + V) and save (Ctrl + S) the following code into your index.py file. <br/>  *(In the code we use our sample credentials but please replace them with your own! <br/>  Here we are creating a cryptocurrency of transaction type 'nvidiacoin'. Ensure you enter a semicolon followed by any version number in your image name e.g. stellar:0.0.1)*

```python
import json
import dragonchain_sdk
dragonchain_client = dragonchain_sdk.Client(dragonchain_id='fcf62a0f-5904-428a-bc7d-99e974fa89e0', auth_key_id='NNIPQSWIKNYV', auth_key='MabBUglfjl87LVLZFJQCahxrKfEQojhc')

# Create a Python Cryptocurrency Contract
print(dragonchain_client.post_contract(
    txn_type='nvidiacoin',
    image='interchain:stellar:0.0.1',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
))
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
            "image": "image_name",
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

# Update Python Smart Contract
print(dragonchain_client.update_contract(
    contract_id='<contract_id>',
    image='image_name',
    cmd='python',
    args=['-m', 'index'],
    execution_order='parallel',
    # auth='<docker_auth_token_if_private_repository>'
))
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
            "image": "image_name",
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
print(dragonchain_client.delete_contract('<contract_id>'))
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
print(dragonchain_client.register_transaction_type('currency'))
```

#### Post a transaction

20) Posting a transaction to currency transaction

```python
# Currency contract
print(dragonchain_client.post_transaction('currency', {
    'version': '1',
    'paymentData': {
        'amount': 500,
        'to': 'John Howies',
        'type': 'dining'
    }
}))
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

21)Post a transaction to our python_contract under the txn_type='example_contract'

```python
print(dragonchain_client.post_transaction('example_contract', {
    'version': '1',
    'exampleData': {
        'type': 'test',
'message': 'Hello, world!'
    }
}))
```

Response from Dragonchain

22) Save the transaction_id returned by your example

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
print(dragonchain_client.register_transaction_type('currency'))
```

#### Query a Transaction

23) Query the currency transaction

Grab the transaction id returned by currency

```python
# # Query currency
print(dragonchain_client.query_transactions(query='your_transaction_id'))
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

24) Query example_contract transaction

Grab the transaction id returned by example_contract

```python
# Query example_contract
print(dragonchain_client.query_transactions(query='your_transaction_id'))
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
### Node example
[Go here](https://github.com/dragonchain-inc/custom-contract-node-sdk)

> Our system also allows developers to add scheduled smart contract execution using a cron expression or seconds between broadcasts. For example, `cron='* * * * *'` and `seconds=59` are both valid. These fields are optional. If you are going to use a scheduler, you can only use a cron or seconds, not both.

### Contribute SDK

Currently, Dragonchain supports two SDKs ([Python](https://github.com/dragonchain-inc/dragonchain-sdk-python) and [Node.js](https://github.com/dragonchain-inc/dragonchain-sdk-node)), but any language could be used to interface with a chain. If you have any questions, concerns, or would like to contribute to a DragonchainSDK or create your own, please join our community developer forum on Telegram (Community Dragonchain Dev Official).
