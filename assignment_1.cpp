#include <iostream>
#include <list>
#include <stdlib.h>

//using namespace std;

// This is our main function
int main()
{
    // A list of ints used as our "bag"
    int marble_bag[]= {1, 2, 3, 4, 5};

    // Then we'll handle removing a random marble.

    // The random number we'll be using to remove a marble.
    int random_num;

    // The random number we'll be using to add a marble.
    int random_num2;

    // This gives us a random number between 1 and 5, or in other words a random marble.
    random_num = rand() % 5 + 1;

    // Then we remove the random marble from the bag.
    marble_bag.remove(random_num);

    // After this we can make another random number between 1 and 5 and add it back to the bag.
    random_num2 = rand() % 5 + 1;
    marble_bag.append(random_num2);


    // The function needs to return something, else the function won't work. The returned value
    // isn't used though.
    return 0;
}