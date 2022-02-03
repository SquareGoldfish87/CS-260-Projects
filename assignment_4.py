#!/usr/bin/env python3
"""Solve basic Calculus sums"""

# In case you don't know, a sum is a while loop.
# It works like this:
# while x != M+1:
    # x += 1
    # plug x into f(x)
    # record the answer
# Then, you add all the values together, and that's the answer.

# We'll need this later.
import random

# First, we'll need a linked list.
# This is the class used for the body of the linked list.
class NumListBody:
    def __init__(self, stored_num):
        self.stored_num = stored_num
        self.next = None

# This is the "head" of our list.
class NumList:
    def __init__(self):
        self.head = None

    # Now we need to define the functions that we'll be using.

    # This is our enqueue function.
    # It places whatever we pass in as "body" as the last item in our list.
    def enqueue(self, body):
        # If there's no list already, this makes whatever you're trying to put on the end
        # the only value.
        if self.head is None:
            self.head = body
        # We skip all body parts in the list, and go straight to the end.
        for current_body_num in self:
            pass
        # Then we add a pointer to the body argument, making it the new last in the list.
        current_body_num.next = body

    # This is the add function.
    # We take 2 arguments aside from self: target and new_body.
    def add(self, target, new_body):
        # We search the list for the body with the target data value we're looking for.
        for body in self:
            # If that body has the target, we set the new body's pointer to the old one's
            # pointer and then make the old body point towards the new body.
            if body.data == target:
                new_body.next = body.next
                body.next = new_body

    # This is the dequeue function.
    # We take the value of the head, set the next body part as the new head, and return the head's value
    def dequeue(self):
        returned_value = self.head.data
        self.head = self.head.next
        return returned_value
        

    # This is the remove function.
    # It works the same as the add function, but instead of adding a new value we're removing
    # the target value and returning it's value.
    def remove(self, target):
        # We'll need to know what the prior body is for this to work.
        # This sets the prior body as the head when we start the function, so everything runs smoothly.
        prior_body = self.head
        # We search the list for the body with the target data value we're looking for.
        for body in self:
            if body.data == target:
                # First we take the data value from the piece we want to remove
                removed_value = body.data
                # Then, we set the prior body's pointer to the current body's pointer.
                # This "removes" the target body, since it's no longer being pointed to.
                prior_body.next = body.next
                return removed_value
            # If the body we're looking at isn't the right one, we set this body as the prior body
            # and check the next one.
            prior_body = body

    # This is the get function.
    # We're once again searching the list the same exact way, but this time we just return the value.
    def get(self, target):
        # We search the list for the body with the target data value we're looking for.
        for body in self:
            if body.data == target:
                # If the body has the value we want, then we return that value.
                returned_value = body.data
                return returned_value

    def insert_first(self, node):
        node.next = self.head
        self.head = node

# This is the test function. It's copy pasted code from further down. It tries to do the below code,
# excepts errors, and prints a statement saying that the copy/pasted code does/doesn't work
def test_function(num_list, k):
    k_2 = k
    k_3 = k_2
    try:
        while k != n+1:
            num_list.enqueue(NumListBody(k))
            k += 1
    # Note: These all have "WhateverError" in them. There is no WhateverError. It's my placeholder way
    # of saying "Whatever error this would normally throw". I can't run it to check, so I didn't fill
    # them in with the actual errors.
    except WhateverError:
        print("Enqueue not functioning.")
    print("Enqueue functioning.")
    counter = 0
    try:
        while counter != 1:
            try:
                body_value = num_list.dequeue()
                answer = equation(body_value)
                sum_list.append(answer)
            except WhateverErrorTypeThisThrows:
                counter = 1
    except WhateverError:
        print("Dequeue not functioning.")
    print("Dequeue functioning.")
    try:
        while k != n+1:
            num_list.add(k-1, NumListBody(k))
            k += 1
    except WhateverError:
        print("Add not functioning.")
    print("Add functioning.")
    try:
        while k_2 != n+1:
            body_value = num_list.get(k_2)
            answer = equation(body_value)
            sum_list.append(answer)
            k_2 += 1
    except WhateverError:
        print("Get not functioning.")
    print("Get functioning.")
    try:
        while k_3 != n+1:
            body_value = num_list.remove(k_3)
            answer = equation(body_value)
            sum_list.append(answer)
            k_3 += 1
    except WhateverError:
        print("Remove not functioning.")
    print("Remove functioning.")
    pass

# Now we need to write out our actual sum.
# For the sake of standardizing things, the variables are going to be named after their math letter 
# equivalents. Check this link to see what I mean.
# https://i.pinimg.com/originals/f2/ed/fd/f2edfd9b2803d32cc7ebf96ec758c324.jpg

# To begin, we need to ask the user for the variables.
# These need to be intergers, so we have to attempt sanitizing the input and ask for a new
# answer if they've put in a non int.
input_checker = 0
while input_checker != 1:
    k = input("Please enter the lower limit of the sum (k): ")
    try:
        k = int(k)
        input_checker = 1
    except ValueError:
        print("Invalid input. Please try again.")
input_checker = 0
while input_checker != 1:
    n = input("Please enter the upper limit of the sum (n): ")
    try:
        n = int(n)
        input_checker = 1
    except ValueError:
        print("Invalid input. Please try again.")


# Next we check to see if we're using test functionality.
test = input("Would you like to run test mode? (y/n): ")
test.lower()
if test == "y":
    num_list = NumList()
    test_function(num_list)

# Here's the function we'll be calling to solve the sum.
# For this example, we'll make it 3x^2.
def equation(num) -> int:
    return_num = 3 * (num)^2
    return return_num
# Due to limitations (see: a lack of time and energy), the equation itself needs to be coded in, 
# rather than us asking the user for it.

# Now we have all our functions and classes, so we can actually compute the sum.

# First, some variables that are shared between the following random outcomes.
# The linked list
num_list = NumList()
# The list our answers will go into
sum_list = []
# A general use counter
counter = 0
# A second k value we'll need later.
k_2 = k

# Since I have way too many functions, this randomly decides whether the sum will be found using
# enqueue/dequeue(1), add/remove(2), or add/get(3).
random_num = random.randrange(1, 4)
if random_num == 1:
    # This is the enqueue/dequeue loop.
    # While k is less than n+1, we add k to our list with the enqueue function.
    while k != n+1:
        num_list.enqueue(NumListBody(k))
        k += 1
    # Now we have our list. To get the sum, we need to remove the values from the list, run them
    # through the "equation" function, and then store that answer somewhere.
    # We remove the front piece of the list, run it through the equation function, add it's value 
    # to a list, and keep doing that until the list is empty, at which point we move on.
    while counter != 1:
        try:
            body_value = num_list.dequeue()
            answer = equation(body_value)
            sum_list.append(answer)
        except WhateverErrorTypeThisThrows:
            counter = 1
    answer = sum(sum_list)
    

elif random_num == 2:
    # This is the add/remove loop.
    # Note: The add and remove functions both require a starting value. We accomplish this by adding
    # k-1 to the linked list. The final answer of this part will be subtracted by this much to ensure
    # the answer is correct.
    num_list.insert_first(NumListBody(k-1))
    # While k is less than n+1, we add it to our list.
    while k != n+1:
        num_list.add(k-1, NumListBody(k))
        k += 1
    # Now that we have our linked list, we need to remove the pieces of the list, return their
    # values, and run those values through the equation function.
    while k_2 != n+1:
        body_value = num_list.remove(k_2)
        answer = equation(body_value)
        sum_list.append(answer)
        k_2 += 1
    answer = sum(sum_list)
        


else:
    # This is the enqueue/get loop.
    # While k is less than n+1, we add k to our list with the enqueue function.
    while k != n+1:
        num_list.enqueue(NumListBody(k))
        k += 1
    # Now we need to get values from the linked list bodies without removing said bodies,
    # return those values, run them through the equation function, etc. You get it by now.
    while k_2 != n+1:
        body_value = num_list.get(k_2)
        answer = equation(body_value)
        sum_list.append(answer)
        k_2 += 1
    answer = sum(sum_list)

# Finally, we print the answer to the user.
print("The sum is: ", answer)
