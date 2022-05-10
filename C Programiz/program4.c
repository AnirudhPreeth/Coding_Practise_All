/*
Multiply Two Floating-Point Numbers
*/

#include<stdio.h>
int main()
{
    float a, b, product;
    printf("Enter two numbers: ");
    scanf("%f %f", &a, &b);
    product = a * b;
    printf("Product is = %f", product);
    return 0;
}

/*
The user is asked to enter two numbers which are stored in variables a and b respectively.
The product of a and b is evaluated and the result is stored in product.

Finally, product is displayed on the screen using printf().

Result is rounded off to the second decimal place using %.2lf conversion character. 

Programiz program: 
#include <stdio.h>
int main() {
    double a, b, product;
    printf("Enter two numbers: ");
    scanf("%lf %lf", &a, &b);  
 
    // Calculating product
    product = a * b;

    // %.2lf displays number up to 2 decimal point
    printf("Product = %.2lf", product);
    
    return 0;
}
*/