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
        self.size = 0

    # Our first operation will be .append()
    def append(self, data):
        self.size += 1
        # We take our data and assign it to our Node
        node = Node(data)
        if self.tail is None:
            self.tail = node  # if our tail does not contain a value, assign our new node to it
        else:
            current = self.tail  # Otherwise we need to iterate through our list until we reach a Null object
            while current.next:
                current = current.next  # Continue to iterate until null object

            current.next = node  # Once Null object is found, assign it with our new nodes

    def length(self):
        return self.size

    def iter(self):
        current = self.tail
        while current:
            value = current.value  # get the value while continuously calling the .next()
            current = current.next
            yield value


# RUNNER TECHNIQUE (If a certain way works multiple times, we call it a technique... and in this case, this is one
# example)
# Finding the kth last element  in the linked list
def kthToLast(head, k):
    p1 = head  # Keep 2 pointers at a starting point
    p2 = head

    for i in range(k):  # Move p1 k times
        if p1 is None:
            return  # Check if it is empty first
        p1 = p1.next  # Move pointer

    while p1 is not None:  # After moving pointer, we are going to iterate until p1 reaches end of list
        p1 = p1.next  # We are moving both pointers simultaneously
        p2 = p2.next

    return p2  # Once p1 has reached the end of the list, we will return p2 (kth to last element)


LinkedList = SinglyLinkedList()
for i in range(9000):
    LinkedList.append(i)

print("Singly Linked List Length is: ", LinkedList.length())

kthElement = kthToLast(LinkedList.tail, 176)
print(kthElement.value)
