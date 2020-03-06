'''
a Binary search tree (BST) is a special kind of binart tree and it is
one of the most important and commonly used data structures in computer
science applications.


A BST is a tree that is structually a binary tree, and stores data in its nodes very efficiently.
It provides very fast SEARCH operations and other operations like: INSERTION AND DELETION


A binary tree is called a bst:

IF value at any node is >= valyes in all the nodes of its left sub-tree and less than or equal to the values
of all the nodes of the right sub-tree.
'''

# of course, we create our Node class with its attributes of left and right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


# To start we will need to keep track of the root node
# Lets make a Tree class that holds that refrence to the root node
class Tree:
    def __init__(self):
        self.root_node = None  # That is all that is needed
    # Lets examine the main operations on the tree (Insert, delete, finding min/max/searching)
    # First, finding the min and max node of the tree (path for min: LEFT CHILD
    #                                                  path for max: RIGHT CHILD)

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child # This is just our standard pointer iteration
        return current # after there are no more left childeren, we found the min and return it

    # Now lets do the same for the max (except for the right child)
    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child # Keep iterating our path of the right child
        return current

    
