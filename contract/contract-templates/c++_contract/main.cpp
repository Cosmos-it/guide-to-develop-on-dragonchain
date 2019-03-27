#include <stdio.h>
#include "contract/handler.h"
#include <iostream>

using namespace std;

int main() {

    char input[2000];
    fgets( input, 2000, stdin);
    string response = handler(input);
    printf("%s",response.c_str());

    return 0;
}
