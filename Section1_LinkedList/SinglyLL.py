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

# But we don't want to keep calling the .next variable so we need something to hold these values...
# This is where singly linked list comes into place...


# We will start by once again, creating a class called SinglyLinkedList
class SinglyLinkedList:
    def __init__(self):
        self.tail = None  # We will always start of with a tail reference and assuming of course that its None

    # Our first operation will be .append()
    def append(self, data):
        # We take our data and assign it to our Node
        node = Node(data)
        if self.tail is None:
            self.tail = node  # if our tail does not contain a value, assign our new node to it
        else:
            current = self.tail  # Otherwise we need to iterate through our list until we reach a Null object
            while current.next:
                current = current.next  # Continue to iterate until null object

            current.next = node  # Once Null object is found, assign it with our new nodes


LinkedList = SinglyLinkedList()
LinkedList.append(5)
LinkedList.append(10)
current = LinkedList.tail  # Start with an entry point

while current:
    print(current.value)
    current = current.next
