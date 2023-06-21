#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** fizzBuzz(int n, int* returnSize){
    char** res = malloc(n * sizeof(char*));
    *returnSize = n;

    for (int i = 1; i <= n; i++) {
        res[i - 1] = malloc(8 * sizeof(char*));

        if (i % 15 == 0) res[i - 1] = "FizzBuzz";
        else if (i % 3 == 0) res[i - 1] = "Fizz";
        else if (i % 5 == 0) res[i - 1] = "Buzz";
        else sprintf(res[i - 1], "%d", i);
    }

    return res;
}
