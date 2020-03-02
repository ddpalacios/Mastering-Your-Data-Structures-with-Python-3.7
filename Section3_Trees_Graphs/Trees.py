# Tree Nodes
# Tree data structures are non linear data structures that store data items in an non-linear order
# a data item can be connectrd to more than on data item.
# In the linear data structures, all of the data items in the linear data can be
# traversed in on pass
# This is NOT possiblr in the case of a nonlinear data structure.

'''
First we will discuss one of most importnt and special inda of trees available,
that is, the BINARY TREE. (A collection of nodes wwhere the nodes in the tree can have 0,1,or 2 child nodes)
A simple binary tree has a maximum of 2 children. (left and right child)


Just like in out preivous implemnetations, a node is a container for data and holds refrenences
to other nodes. In a binary tree, those refreneces are the left and right child

So lets see how the node class may look like for a bianry tree:
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
# to test this, we must first create our nodes and connect them together
n1 = Node("Root Node")
n2 = Node("left child Node")
n3 = Node("right child Node")
n4 = Node("Left grandchild Node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

current = n1
while current:
    print(current.data)
    current = current.left_child

