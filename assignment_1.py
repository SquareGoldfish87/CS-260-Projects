#!/usr/bin/env python3
# The above is the shebang. It helps the file open on Linux, I belive.

# First we import random
import random

# Then we make the bag of marbles.
marble_bag = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# This introduces the user to the program and asks which action they'd like to perform.
print("Welcome to PyMarble!")
print("Would you like to take a marble out of the bag or put a new one in?")

# This checks to see if the input is one we care about.
user_input = input("Take out/place inside [t/p]: ")
# This makes the letter lowercase if it isn't already.
user_input.lower()
print("This is the current bag:")
print(marble_bag)
# If the user wants to take a marble out, then we remove a marble at random.
if user_input == "t":
    print("Removing marble...")
    # Worth noting: We need the random number to be 0-8 because we're removing items based on index.
    random_num = random.randrange(0, 8)
    # Then we delete the number from the list, using the random index.
    del marble_bag[random_num]
    # Also worth noting: When we print the removed number to the user, we need to add 1 to it
    # because the random_num is the index, not the number itself.
    print(f'The marble you pulled is {random_num+1}')
    # Then we print the list to the user again.
    print("The current bag is:")
    print(marble_bag)
# If the user wants to put a marble in, then we add a new marble at random.
elif user_input == "p":
    print("Placing marble...")
    # This number has to be 1-9 because it's being added directly, not being used for index reasons.
    random_num = random.randrange(1, 9)
    # Then we append the number to the list.
    marble_bag.append(random_num)
    print("This is the current bag:")
    print(marble_bag)
else:
    print("Invalid input. Please try again.")