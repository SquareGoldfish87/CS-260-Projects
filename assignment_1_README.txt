In your README file (feel free to include labeled drawings!) explain what a program could do to 
model a bag of marbles, with a list of properties (variables) and behaviors (methods), including
 at least something like the following:

some way of representing marbles (what makes up a marble in this program?),

I haven't much experience in C++ (see: none), but assuming there are lists, then we can use a list
for our bag. In which case, we can use numbers for marbles. Maybe it's even possible to create
unique attributes for each marble, like a marble class that remembers things about itself
(say, Marble #1 is red and large, Marble #387 is peuce and microscopic, etc). However, that seems
a touch complex, and simple implementation is the name of the game here. We could also use strings
for marbles (red, red, blue, green, red, green, etc.).

a way to add new marbles into the bag (how do we interact with marbles and add them into the bag?),

If there's a way to append a list, we can put the marbles back into the bag after they're drawn, or
we can add marbles to the bag after it's creation.

a way to remove a marble out of the bag (perhaps a random marble taken out of the bag?),

Assuming the lists work off of indexes, and there's a way to remove an item from a list 
if you know it's index, then we're just fine. If a .random sort of thing is in C++ (which is to say,
a way to get a random int between certain specific values), then random marble draws should be
possible.

a few ways that we could use to show that our implementation should be working correctly (tests),

We could do really any of the following:
Run the program as intended
Try and take out a marble that doesn't exist (say, a 4th marble if the bag only has 3)




We can make a "bag" of a set length/set colors. If we can randomize that list, then we can iterate
over the new list and "pull out" a marble.
