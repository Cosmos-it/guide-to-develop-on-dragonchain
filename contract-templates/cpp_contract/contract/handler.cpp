#include <stdio.h>
#include "handler.h"

std::string handler(std::string payload) {
    fprintf(stderr, "This is a log\n");
    std::string returnValue = "Hello from cpp smart contract: " + payload;
    return returnValue;
}
