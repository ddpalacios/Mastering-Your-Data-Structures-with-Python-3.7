# Now that we covered Singly Linked List, Our next implementation will be Doubly Linked List
# Unlike Singly Linked List, a doubly linked list will allow us to move forward and backwards within a list
# Which is a significant improvement. So, lets try and implement this.

# Once again, lets start implementing our Node class except with a few modifications
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None  # We are now adding a prev variable to our Node class


# DLL -->  1 <=> 2 <=> 5 <=> 3 ...

# Same procedure, lets see how this works dynamically...
a = Node(1)
b = Node(10)
c = Node(20)
d = Node(30)

a.next = b
b.next = c
c.next = d
d.prev = c
c.prev = b
b.prev = a


# print(a.next.value, a.next.prev.value) # Whats the output?
# Output: 10 1

# Now lets start implementing the class ..
