#include <stdio.h>
int main(void)
{
    int a;
    printf("Enter an input1: ");
    scanf("%d", &a);
    printf("Your input is: %d\n", a);

    int b;
    printf("Enter an input2: ");
    scanf("%d", &b);
    printf("Your input is: %d\n", b);

    int c;
    printf("Enter an input3: ");
    scanf("%d", &c);
    printf("Your input is: %d\n", c);
printf("Average: %d", (a + b + c) / 3);
}
