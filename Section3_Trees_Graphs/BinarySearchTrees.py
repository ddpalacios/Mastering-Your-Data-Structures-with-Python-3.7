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
            current = current.left_child  # This is just our standard pointer iteration
        return current  # after there are no more left childeren, we found the min and return it

    # Now lets do the same for the max (except for the right child)
    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child  # Keep iterating our path of the right child
        return current

    # One the most important operations to implement is to insert data items in the tree
    # We have to keep in mind that BST have a certain criteria of how BST nodes are stored
    # A quick run through:
    '''
    The left child nodes should contain the data less than their own value and the right
    child should have data greater than their value
    So we have to ensure that the property if the BST satisfies whenever we insert an item
    in the tree.
    '''

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:  # First check if we have a root
            self.root_node = node
        else:
            # We need to keep track of the curr node. as well as the parent.
            # We use a current variable to be used for that purpose
            current = self.root_node
            parent = None
            while True:
                parent = current

                # from here, we need to perform comparisons in order to maintain
                # a proper binary search tree
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return

                # Now we have to take care of the greater than or equal case.
                # if the current node does not have a right child then the new node
                # is inserted as the right child node. Otherwise we move down and continue
                # looking for an insertion point
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

                # Insertion takes O(h) where h is the height of the tree
