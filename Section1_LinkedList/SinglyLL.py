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

    def delete(self, tgt_data):
        # We want to delelte a node that is btwn two other nodes, all we have to
        # do is make the prev node to the successor of its next node that is to
        # be deleted.
        current = self.tail # We use current var in order to find our target data
        prev = self.tail  # Two pointers as starting point. Current and previous
        while current is not None:  # While there is data in the current node

            if current.value == tgt_data:  # if we found our target from our current node
                if current == self.tail:  # if the current node is our beginning tail node (First node)
                    self.tail = current.next  # then we want our tail to be the next preceding node as our tail instead
                else:
                 
                    prev.next = current.next  # If its not, our previous node will point to the node of the current node
                self.size -= 1  # decrement our LL size
                return  # Return none

            # Continue iterating and updating our variables
            prev = current  # The current node is now set to be a prev node
            current = current.next  # the next node after the current one (This is just simple LL iteration)
            # Time complexity of deleting this node is O(n)


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


# Deleting a node without a refrence to the head pointer
def deleteNode(tgt_node):
    if tgt_node is None or tgt_node.next is None:
        return False
    next_node = tgt_node.next
    tgt_node.value = next_node.value
    tgt_node.next = next_node.next
    return True


LinkedList = SinglyLinkedList()
for i in range(5):
    LinkedList.append(i)

print("Singly Linked List Length is: ", LinkedList.length())

LinkedList.delete(0)
LinkedList.delete(4)
LinkedList.delete(3)
for each_elem in LinkedList.iter():
    print(each_elem)


print("Singly Linked List Length is: ", LinkedList.length())