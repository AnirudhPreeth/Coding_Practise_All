/*
ASCII Value of a Character.
*/

#include<stdio.h>
int main()
{
    char c;
    printf("Enter a character: ");
    scanf("%c", &c);
    printf("ASCII value of %c = %d", c, c);
    return 0;

    // %c -> Displays the integer value of the character.
    // %d -> Displays the actual character. 
}

/*
The user is asked to enter a character. The character is stored in variable c.

Suppose you type in character -> G.
Then...

When %d format string is used, 71 (the ASCII value of G) is displayed.
When %c format string is used, 'G' itself is displayed.
*/
