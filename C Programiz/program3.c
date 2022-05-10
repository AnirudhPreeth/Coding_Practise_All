/*
Program to Add Two Integers.
*/

#include<stdio.h>
int main()
{
    int number1, number2, sum;
    printf("Enter two integers: ");
    scanf("%d%d", &number1, &number2);
    sum = number1 + number2;
    printf("%d + %d = %d", number1, number2, sum);
    return 0;
}

/*
The user is asked to enter two integers. 
These two integers are stored in variables number1 and number2 respectively.

Then, these two numbers are added using the + operator, and the result is stored in the sum variable.
Finally, the printf() function is used to display the sum of numbers.
*/