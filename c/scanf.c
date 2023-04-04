#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    char s[4];
    printf("What is your name: ");
    scanf("%s", &s);
    printf("Have a nice day: %s\n", s);
}