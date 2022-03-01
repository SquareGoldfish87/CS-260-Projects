#!/usr/bin/env python3
"""Create 2 hashtables"""

# We'll be making 2 hashtables. One is going to overwrite an old value with a new value if it comes up,
# and one will instead make both values coexist.

# First, we need to define some functions

# This will be our hash equation. The way we determine where we're placing items will be through a 
# modulo operation.
def hash_equation(value, list_length):
    """Compute a value and return it."""
    returned_value = value % list_length
    return returned_value

# To my understanding, a hash table is just a dictionary but you compute where each value goes based on
# some random arbitrary thing. As such, I'll be placing my results into a dictionary.

# This is a "shortcut" function that constructs a dictionary automatically.
# Just pass in a list of values you'd like to hash and this does the rest.
def hashtable_maker(value_list) -> list:
    """Take the results from hash_equation and place them into a dictionary."""
    # We'll need a list of keys, a list of values, and the length of the list.
    keys = []
    values = []
    list_length = len(value_list)
    # For every value in the passed through list, we append our value to the values list and append
    # our hashed value to the index list.
    for value in value_list:
        values.append(value)
        hash_value = hash_equation(value, list_length)
        keys.append(hash_value)
    # Then, we zip the lists together into a dictionary and return that dictionary.
    hashtable = dict(zip(keys, values))
    return hashtable

# In this case, if we had a list of values that made 2 values assign to the same key, the first 
# value would be overwritten. So, let's make a second function that handles this better.

def smarter_hashtable_maker(value_list) -> list:
    """hashtable_maker but with the ability to handle 2 items at the same index."""
    # Much of the code is the same. We still need the list length, plus an empty dictionary
    # and an empty list.
    hashtable = {}
    list_length = len(value_list)
    double_hash_value = []
    # This time, things are slightly different. For starters, I remembered how to actually make a 
    # dictionary so we won't be using a zip.
    for value in value_list:
        # We still need our hash value.
        hash_value = hash_equation(value, list_length)
        # If the index we're about to assign is already in the dictionary, we have conflicting
        # hash values. So, we take the value at that index that's already in the dictionary,
        # and the value we want to put at that index, place them both in a list, and then put
        # that list at the index.
        if hash_value in hashtable:
            # value_1 is the current value at the index
            # value_2 is the new value we want to assign
            value_1 = hashtable[hash_value]
            value_2 = value
            # If there's already a list at that index, we just need to append the new value.
            if value_1 is list:
                double_hash_value.append(value_2)
            # Otherwise, we append both values.
            else:
                double_hash_value.append(value_1)
                double_hash_value.append(value_2)
            # Then we append this new list to the dictionary.
            hashtable[hash_value] = double_hash_value
        # If the hash value isn't already in the dictionary (the usual case) then we just
        # append the value at the proper key.
        else:
            hashtable[hash_value] = value
    # Finally, we return our hash table.
    return hashtable


# Because we're using a dictionary, chaining is actually entirely unnecessary. If we encounter
# multiple values that should be in the same place, we can just assign a list containing all the
# values at that index to the index in question (which is what I did. Work smarter, not harder and
# all that).

# This is where user output is handled. If you want to see a different set of numbers be hashed, 
# switch the below numbers out for something else. 

# This example happens to create a conflict, so if that's what you're here to see then run it as is.

print("The first hashtable maker prints this:")
print(hashtable_maker([3,2,9,11,7]))

print("The smarter hashtable maker prints this:")
print(smarter_hashtable_maker([3,2,9,11,7]))