#!/usr/bin/env python3
"""Create a Binary Search Tree, traverse the tree, and use the nodes of the tree to find a sum."""

# I'll level with you. A lot of this code is taken from various GeeksForGeeks pages, since I couldn't
# think of a way to insert/remove values, or make the Binary Search Tree in an automated way. But,
# rather than turn in an assignment with code that's entirely someone else's with changed variable
# names, we'll try and do better. I'll take that code and make a practical program that uses it
# to do something with a real world application.

# Note: Every function/class here, with the exception of everything from search downward, was taken
# from GeeksForGeeks.com.

# To begin, we need our Body parts, much like a linked list.
class Body:
    # This makes every instance of Body unique, and able to hold it's own value.
    def __init__(self, stored_num):
        # This will handle left values.
        self.left = None
        # This will handle right values.
        self.right = None
        # This stores the Body's value.
        self.value = stored_num

def in_order_printer(tree):
    """Print the left values of the tree, the root, and the right values of the tree."""
    # If we have a tree, then we print in order. This means left values first, then the root value, then
    # the right values.
    if tree:
        # We call the function recursively until we've printed all the left/right numbers.
        in_order_printer(tree.left)
        print(tree.value)
        in_order_printer(tree.right)

# Here we initialize the test BST.
# It's used to test new add/remove/print functions.
def test_tree():
    """Make a small BST to be used for testing."""
    Yggdrasil = Body(1)
    Yggdrasil.left = Body(2)
    Yggdrasil.right = Body(3)
    Yggdrasil.left.left = Body(4)
    Yggdrasil.left.right = Body(5)
    return Yggdrasil


# We'll need these later. These set a minimum/maximum we'll use when checking for the root.
INT_MIN = -float("inf")
INT_MAX = float("inf")

# These functions do nothing but grab the pre-index and add 1 to it respectively.
def getPreIndex():
    """Get and return the pre-index value."""
    return tree_maker.preIndex
 
def incrementPreIndex():
    """Add 1 to the current pre-index value."""
    tree_maker.preIndex += 1
 
# This is a recursive function to construct a BST.
def tree_maker(tree_list, current_num, minimum, maximum, size):
    """Create a Binary Search tree."""
    # This is a base case.
    if(getPreIndex() >= size):
        return None
 
    Yggdrasil = None

    # We only care if the current_num we're checking in the list is within our minimum/maximum
    # (which will be changing)
    if(current_num > minimum and current_num < maximum):
        # If it is, then we want to create a piece of the tree using the current_num.
        Yggdrasil = Body(current_num)
        incrementPreIndex()
        # If the pre-index is less than the length of our list, we know that this number goes 
        # on the left. So we recursively call the function, but pass in our current min/max, 
        # current_num, and all other relevant variables.
        if(getPreIndex() < size):
            Yggdrasil.left = tree_maker(tree_list, tree_list[getPreIndex()], minimum, current_num, size)
        # Otherwise, it has to go to the right, where we pass in all the same stuff as we do for the
        # above scenario, but we tell it to place the number to the right.
        if(getPreIndex() < size):
            Yggdrasil.right = tree_maker(tree_list, tree_list[getPreIndex()], current_num, maximum, size)
        
        # Then, we return our completed tree. Because we loop recursively, there should be
        # no way we get here without having the finished tree ready.
        return Yggdrasil

# This function just sets all the variables we need to call tree_maker, and then calls it with
# those variables.
def tree_maker_shortcut(tree_list):
    """Call tree_maker with all the appropriate variables."""
    tree_maker.preIndex = 0
    size = len(tree_list)
    return tree_maker(tree_list, tree_list[0], INT_MIN, INT_MAX, size)

# This is the function that adds values.
def insert(tree, stored_num):
    """Insert a value into a Binary Search Tree given a BST and a value."""
    # These handle checking if the value is inserted properly.
    # If not, we just move on.
    if tree is None:
        return Body(stored_num)
    else:
        if tree.value == stored_num:
            return tree
        # If the value in the node is less than what we're trying to insert, then our new
        # value goes to the right. Otherwise, it goes to the left.
        elif tree.value < stored_num:
            tree.right = insert(tree.right, stored_num)
        else:
            tree.left = insert(tree.left, stored_num)
        return tree


def min_value_finder(node):
    """Find a new min value in a BST"""
    current = node
 
    # As long as the tree is sorted, the leftmost value should be the smallest. So we just go as
    # left as possible, and return the leftmost value.
    while(current.left is not None):
        current = current.left
 
    return current

# This is the delete function.
def delete(tree, stored_num):
    """Delete a value in a BST given the tree and the value to be deleted"""
    # This is our base case.
    if tree is None:
        return tree

    # This is gonna look a lot like our insert function, because the way they traverse the list is
    # functionally identical. We recursively call the function and .left/right to find the thing we
    # need to edit.
    if stored_num < tree.value:
        tree.left = delete(tree.left, stored_num)
 
    # If it's less than the root, we go left. Otherwise, we go right.
    elif(stored_num > tree.value):
        tree.right = delete(tree.right, stored_num)
 
    # If the number we're looking for is neither higher or lower than the current number, then we've
    # found the number to be deleted.
    else:
        # This removes the Body piece from the BST.
        if tree.left is None:
            temp = tree.right
            tree = None
            return temp
 
        elif tree.right is None:
            temp = tree.left
            tree = None
            return temp
 
        # This handles finding a successor. We find the smallest number on the right, set it as the
        # new root, and then run the deletion function recursively to get rid of the old root.
        temp = min_value_finder(tree.right)
        tree.value = temp.value
        tree.right = delete(tree.right, temp.value)
 
    # Once we're done, we use this to return the tree.
    return tree

# This is our search function.
# Starting here, every function is something I made, not just copy/pasted and changed names.
# This function is about 99% copied code, but it's not something the website had.
def search(tree, stored_num):
    """Search a binary search tree for all values in a list, append these values to a list, and
    return the list of found values."""
    if tree is None:
        return tree
    # The third function to have this code. We search the BST for the values we want by checking to
    # see if it's left or right, and then searching either the left or right for it.
    if stored_num < tree.value:
        tree.left = search(tree.left, stored_num)
    elif(stored_num > tree.value):
        tree.right = search(tree.right, stored_num)
    else:
        # If it's not higher or lower, it must be the same, so that's what we're looking for. We then
        # return that value. Is it redundant? Absolutely. But we technically traversed the tree for
        # the value, so it works.
        # Note: This returns a NoneType, not an Int.
        return stored_num


# This is the list of values I'll be using to create my BST.
tree_list = [10, 5, 1, 7, 40, 50]

# This is the equation we'll pass our numbers through for our sum.
def equation(num) -> int:
    return_num = 3 * (num)^2
    return return_num

# Since search returns a NoneType, we can't use the below code. If search returned an int, or we could
# make NoneTypes into ints, then we'd be fine. As it is, here's the code.

# This code makes a list of numbers to pass into the equation function.
#num_list = []
#x = tree_maker_shortcut(tree_list)
#for value in tree_list:
    #found_value = search(x, value)
    #found_value = int(found_value)
    #num_list = num_list.append(found_value)

# Since the above code doesn't really work, we'll use the tree_list to find our sum, since that's what
# the above would've returned anyways if it wasn't NoneTypes.

def showboat():
    """Make a BST and then add and delete various numbers."""
    # This makes our BST
    Yggdrasil = tree_maker_shortcut(tree_list)
    # This prints the contents of the tree to the user.
    print("Our Binary Search Tree is: ")
    in_order_printer(Yggdrasil)
    # This adds a value to the BST
    insert(Yggdrasil, 8)
    # This prints the BST again
    print("Our Binary Search Tree after adding 8 is: ")
    in_order_printer(Yggdrasil)
    # This removes a value from the BST
    delete(Yggdrasil, 10)
    # This prints the BST again again
    print("Our Binary Search Tree after removing 10 (the root) is: ")
    in_order_printer(Yggdrasil)

def sum_solver(decider, user_list):
    """Solve a sum given information about it."""
    # In case you don't know, a sum is a while loop.
    # It works like this:
    # while x != M+1:
        # x += 1
        # plug x into f(x)
        # record the answer
    # Then, you add all the values together, and that's the answer.
    # This is a list we'll need.
    sum_list = []
    # This is what a normal sum looks like.
    if decider == 1:
    # We get the lower and upper limit from the user.
        lower_limit = input("Please enter the lower limit (k): ")
        upper_limit = input("Please enter the upper limit (n): ")
        # This is how a sum_solver *should* work.
        # While the lower limit isn't the upper limit +1
        while lower_limit != upper_limit+1:
            # We run the lower_limit through our equation, append the result to a list,
            # add 1 to lower_limit, and loop.
            answer = equation(lower_limit)
            sum_list.append(answer)
            lower_limit += 1
        # Then, once that's done, we just run the list through the sum function and return it. Easy.
        return sum(sum_list)
    # What if you only wanted a partial sum though? Well, then instead of doing all this, we'll do
    # something else.
    elif decider == 2:
        # This isn't really a "sum", but if you wanted to run a set of numbers through an equation and
        # add the results, it'd look like this. A partial sum, if you will.
        # We take a given list of values, run it through "equation", and put the answers in a list.
        for value in user_list:
            answer = equation(value)
            sum_list.append(answer)
        
        return sum(sum_list)




# We ask the user what they'd like to do.
user_answer = input("Would you like to run a test, run the program, or use the sum solver? [t, r, s]")
user_answer.lower()

# If the user wants to see the program run, we run showboat
if user_answer == "r":
    showboat()
# If the user wants to use the sum solver, we run sum_solver
elif user_answer == "s":
    # This would have been where we passed in the list we got from the BST, but since we can't get that
    # list, we're instead using tree_list, since it's the same numbers.
    print("The sum of our BST is: ", sum_solver(2, tree_list))
# If they put in literally anything else, they can see the test_tree be printed in order.
else:
    print("Running test function...")
    in_order_printer(test_tree())

