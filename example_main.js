const dragonchainClient = require('dragonchain-sdk')
// dragonchainClient.setLogger(console);

const main = async () => {
    const client = await dragonchainClient.createClient({
        dragonchainId: 'your_dc_id',
        authKeyId: 'your_authkeyId',
        authKey: 'your_authkey',
        endpoint: 'https://your_dc_id.api.dragonchain.com'
    });

    // Post a contract
    response(await client.createSmartContract({
        transactionType: "contract_name",
        image: 'image_name',
        cmd: 'node',
        args: ['index.js'],
        execution_order: 'parallel',
        // registryCredentials: ''
    }));

    // Update a contract: 
    // response(await client.updateSmartContract({
    //     smartContractId: 'contract_id',
    //     image: 'image_name',
    //     cmd: 'node',
    //     args: ['index.j],
    //     executionOrder: 'parallel',
    //     environmentVariables: 'provide_here',
    //     secrets: "",
    //     registryCredentials: ''
    // }));

    // To post smart contract written in different languages, 
    // change the cmd and args values.

    // -----------------------
    // Posting Python contract
    // cmd:'python',
    // args:['-m', 'index'],

    // -----------------------
    // Posting Go contract:
    // cmd:'./main',
    // args:[''],

    // ------------------------
    // Posting C/C++ contract:
    // cmd:'./main'
    // args:['']

    // -----------------------
    // Posting C# contract:
    // cmd:'dotnet',
    // args:['root.dll'],

    // ------------------------
    // Posting Shell contract:
    // cmd:'sh',
    // args:['contract.sh'],
    // 
}

const response = async (transaction) => {
    if (transaction.ok) {
        console.log(JSON.stringify(transaction.response, null, 2));
    } else {
        console.log('Something went Bazooka');
        console.error(`HTTP status code from chain: ${transaction.status}`);
        console.error(`Error response from chain: ${transaction.response}`);
    }
}


//  call main
main();