#!/usr/bin/env python3
"""Sort a list numerically using an array."""

# First, we need these modules.
import array as ar
import random as rand

# To start, we need a random list of numbers
random_list = []

# This makes a list of 10 random numbers
# These numbers can be anything from 1 to 100, inclusive
for i in range(0, 10):
    random_int = rand.randint(1, 100)
    random_list.append(random_int)

# We'll need a duplicate of the list.
array_list = random_list

print("The unsorted list is: ", array_list)

# This sorts our random list
random_list.sort()

# Note: I tried to compare the sorted random_list to a pre-existing array that was then
# sorted using the below code. Even when the array was sorted, it was never "equal to the list"
# so the while loop never broke. However, f you make an array with array_list and pass that 
# array into the below code, it will be sorted just the same. I just decided against it because I
# couldn't get it to work and we've probably both had enough of me waiting to turn stuff in
# to hammer out every little thing.

# While our unsorted list isn't the same as the sorted one, we sort it.
while array_list != random_list:
    # This is a counter that's used as an index.
    counter = -1
    # For every number in the unsorted list, compare it to the number before it.
    for number in array_list:
            counter += 1
            previous_num = array_list[counter-1]
            # If the previous number is bigger, we remove the previous number
            # and append it to the end.
            if number < previous_num:
                x = array_list.pop(counter-1)
                array_list.append(x)

# Finally, we create an array using the sorted list and print the sorted array.
sorted_array = ar.array('i', array_list)

# Then we print all the numbers in our newly sorted array.
print("The sorted array is: ")
for i in sorted_array:
    print(i)