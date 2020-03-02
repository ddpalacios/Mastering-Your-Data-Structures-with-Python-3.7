# Stacks are introduced as a Last In First Out structure (LIFO)
# Stacks allow us to keep track of the return address during fiunction calls

# Stacks are brought upon a similar structure as a Singly Linked list
# So we will start of with our standard Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Unlike the Singly Linked List class, we need to implement two operations:
# Push() - Used to add an element at the top of a stack
# Pop() - Returns the topmost elemtn of the stack and returns None if the stack is empty

# Lets start by making our class the same as before
class Stack:
    def __init__(self):
        self.top = None # Instead of head/tail, we use TOP
        self.size = 0 # To keep track of the lenght of the Stack

    def push(self, data):
        # Of course, first we must create our Node object
        node = Node(data)

        # if the stack has elements:
        if self.top:
            # new node must have its NEXT pointer pointing to that node that was at top earlier
            node.next = self.top
            # We put this new node at top of stack by pointing self.top to new node
            self.top = node

        # otherwise just point TOP to new node
        else:
            self.top = node

        self.size+=1 # Increment length


        


