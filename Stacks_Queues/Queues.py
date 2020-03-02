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

