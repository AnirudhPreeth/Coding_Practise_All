/*
Print Number Entered by User. 
*/

#include<iostream>
using namespace std;

int main() {
    int number;
    cout<<"Enter an integer : ";
    cin>>number;

    cout<<"You entered : "<<number;
    return 0;

}

/*
When the user enters an integer, it is stored in variable number using cin.
Then it is displayed on the screen using cout.

We will be using the std namespace using the code: using namespace std;
Allowed us to write : cout, cin, endl etc, instead of std::cout and std::cin, std::endl.

This is simply to make our code cleaner and more readable.
*/