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
        current = self.tail  # We use current var in order to find our target data
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


# Deleting a node without a reference to the head pointer
def deleteFrom(tgt_node):
    if tgt_node is None or tgt_node.next is None:
        return False
    tgt_node.value = tgt_node.next.value
    tgt_node.next = tgt_node.next.next
    return "Node is deleted!"


def combine_partition(List):
    head, tail = None, None
    for each_elem in List:
        node = each_elem
        if head:
            head.next = node
            head = node
        else:
            tail = node
            head = node

    return tail, head


def partition(partition_number, original_tail):
    current_node = original_tail
    left_part, right_part = [], []
    while current_node:
        if current_node.value < partition_number:
            left_part.append(current_node)
        elif current_node.value >= partition_number:
            right_part.append(current_node)

        current_node = current_node.next

    left_tail, left_head = combine_partition(left_part)
    right_tail, right_head = combine_partition(right_part)

    left_head = right_tail
    right_tail.next.next.next = None

    return left_tail


tail = Node(3)
n1 = Node(5)
n2 = Node(8)
n3 = Node(5)
n4 = Node(10)
n5 = Node(2)
n6 = Node(1)

tail.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

new_tail = partition(5, tail)

while new_tail:
    print(new_tail.value)
    new_tail = new_tail.next

tgt_node = tail.next.next

print(deleteFrom(tgt_node))
current = tail
while current:
    print(current.value)
    current = current.next

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


class NodeStack:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = NodeStack(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None


# Check if a linked list is a palindrome
def check(linkedlist):
    stack = Stack()
    size = linkedlist.size
    tail = linkedlist.tail
    res1, res2 = "", ""
    for first_half in range(size // 2):
        res1 = res1 + str(tail.value)
        tail = tail.next

    for second_half in range(size // 2):
        tail = tail.next
        stack.push(str(tail.value))

    for i in range(stack.size):
        val = stack.pop()
        res2 = res2 + val

    print(res1, '\t\t', res2)
    if res1 == res2:
        return True
    else:
        return False


if __name__ == "__main__":
    linkedlist = SingleLinkedList()
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.append(90)
    linkedlist.append(90)
    linkedlist.append(4)
    linkedlist.append(5)
    linkedlist.append(5)
    linkedlist.append(5)
    linkedlist.append(4)
    linkedlist.append(3)
    linkedlist.append(2)
    linkedlist.append(1)

    print(check(linkedlist))
