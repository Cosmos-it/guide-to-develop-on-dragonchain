### Getting started with smart contract

##### Docker commands: 
	

Build local: 

```
docker build -t <your_docker_hub_username>/<contract_name> .
```

Test the contract:
This will check your smart contract locally before publishing it, once a docker image is created. 
This example uses a sample smart contract docker image written in Go.


Lets 
```
 docker run -it taban/cplus_contract sh
```
Publish to docker repo: 

```
docker push <your_docker_hub_username>/<contract_name>:latest
```
	
#### Using Dragonchain SDKs: 
	
> Python SDK:
   ```python

	import json
	from dragonchain_sdk import dragonchain_client

	client = dragonchain_client.Client("<DC_ID>","<AUTH_KEY>","AUTH_KEY_ID")

	# Posting NodeJs contract
	print(json.dumps(client.post_contract(
		txn_type='node_contract',
		image=<docker_username>/<contract_name>:latest
		cmd='node',
		args=['-m', 'index'],
		execution_order='parallel'
	)))

	# Updating NodeJs contract
	print(json.dumps(client.update_contract(
		txn_type='node_contract',
		image=<docker_username>/<contract_name>:latest
		cmd='node',
		args=['-m', 'index'],
		execution_order='parallel'
	)))

   ```
   
   > NodeJs SDK:
   
   
   ```javascript
	const { DragonchainClient} = require('dragonchain-sdk')
	const dragonchainClient = new DragonchainClient("Dragonchain_id") // Replace with your actual chain id
	dragonchainClient.overrideCredentials("authKeyId", "authKey"); // Replace with your actual keys
	
	// Posting NodeJs contract
	try{ 
		response(await dragonchainClient.post_contract(
		txn_type='node_contract',
		image=<docker_username>/<contract_name>:<latest>
		cmd='node',
		args=['-m', 'index'],
		execution_order='parallel'));
	}catch (e ){
		console.log("Error");
	}

	try{ 
		response(await dragonchainClient.update_contract(
		txn_type='node_contract',
		image=<docker_username>/<contract_name>:latest
		cmd='node',
		args=['-m', 'index'],
		execution_order='parallel''));
	}catch (e ){
		console.log("Error");
	}
   ```
