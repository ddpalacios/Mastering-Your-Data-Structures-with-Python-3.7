# Implement a singly linked list that appends several elements

# So to start, a singly linked list contains nodes as objects with two attributes:
#  Next()
# value()


class Node:
    def __init__(self, data):  # A node needs allows any type of data to be initialized
        self.value = data
        self.next = None  # next can hold any type. So objects will be able to hold for this attribute


# So for example, to get an idea how this works, lets  initialize a few nodes and create links between them...
a = Node("Hello")
b = Node("There")
c = Node("Okay")
d = Node("Bye!")
# here we initialized our nodes, lets link them together...
a.next = b  # a -> b
b.next = c  # b -> c
c.next = d  # c -> d
# a points to b and b points to c and so forth...

# lets print this out...

# print(a.next.next.next.value) # What will the output be?
# Output: Bye!

# But we dont want to keep calling the .next variable so we need something to hold these values...
# This is where singly linked list comes into place...



