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

[Using SDKs](https://github.com/dragonchain-inc/guide-to-develop-on-dragonchain/wiki/SDKS)
