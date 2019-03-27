#include <stdio.h>

int main() {
    char input[2000];
    fgets( input, 2000, stdin);
    printf("%s",input);
    return 0;
}
