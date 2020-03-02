# Queues data structures is very simular to the regualar Queue you are ccustomed to in real life
# Queues use a FIFO data structure (first in first out)
# Queues can be implemented using various methods such as list, stack, and nodes.

# We will start implementing a Queue using a LIST

# Queue LIST implementation
class ListQueue:
    def __init__(self):
        self.items = [] # Queue is empty when we create it
        self.size = 0 # Again, to keep track of the size

    # Enqueue and Dequeue are two important operations in a Queue implementation

    # Enqueue implementation:
    def enqueue(self, data):
        self.items.insert(0, data) # We use the .insert() method to always to append data to index 0
        self.size +=1

    # Dequeue operation
    def dequeue(self):
        # Used to delete items from the queue
        # This method returns the topmost item from the queue and deletes it from the queue
        data = self.items.pop()
        self.size -= 1
        return data


# Queues can also be implemented using two stacks.
# These stacks will help us to implement  a queue
class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    # Enqueue operation
    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        # Instead of remocing elements from the inbound stack
        # we shift our attention to another stack that is outbound stack
        # we shall delete the elements from our queueu only through the outbound stack
        if not self.outbound_stack: # if the outbound stack is not empty...
            while self.inbound_stack: # Then while there are elements in the inbound stack...
                self.outbound_stack.append(self.inbound_stack.pop()) # Pop off the elements and append in outbound stack
        return self.outbound_stack.pop()

# We are trasfering elements between two python lists
queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
# print(queue.inbound_stack) # Output: [5, 6, 7]
queue.dequeue()
# print(queue.inbound_stack) # Output: []

# print(queue.outbound_stack) # Output: [7, 6]
queue.dequeue()
# print(queue.outbound_stack) # Output: [7]


# Node Based Queues implementation

# A queue can be implemnted using a doubly linked likst, and insertaion and deletion operation on this data structure
# Has complexity of O(1)

# A Double Linked list can be treated as a queue if it enables a FIFO kind of data access

# So lets once again, Start of with a node class just like a doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class NodeQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Enqueue operation
    # The enqueue method is similar to the append operation of doubly linked list
    # It creates a node from the data passed to it and appends it to the tail aof the queue
    # and points both head and tail to the newly created node if the queue is empty
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size+=1

    # Dequeue operation
    # This method removes the node at the front of the queue.
    # to remove the first element pointed to by self.head, an if statement is used:
    def dequue(self):
        current = self.head
        if self.size == 1:
            self.size -=1
            self.head = None
            self.tail = None
        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1




