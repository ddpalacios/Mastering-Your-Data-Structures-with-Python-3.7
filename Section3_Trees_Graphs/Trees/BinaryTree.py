# Tree Nodes
'''
Tree data structures are non linear data structures that store data items in an non-linear order
a data item can be connectrd to more than on data item.
In the linear data structures, all of the data items in the linear data can be
traversed in on pass
This is NOT possible in the case of a nonlinear data structure.


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

# Notice that we are iterating through only one side of the tree
# Could we possibly traverse through the entire tree?
current = n1
while current:
    print(current.data)
    current = current.left_child

# This is where tree traveral comes into place.
# And this can be done eaither:
# - Depth-first search (DFS)
# - Breadth-first search
# we will first go over the three types of Depth first search:
'''
- in-order
- pre-order
- post order
'''
class Tree:
    def __init__(self):
        self.root_node = None  # That is all that is needed


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
                if not parent.left_child:
                    parent.left_child = node
                if not parent.right_child:
                    parent.right_child = node
                if parent is None:
                    return



class LinkedList:
    def insert(self, data):
        pass




from collections import deque

def LL_from_depth(root):
    traversal_queue = deque([root])
    while len(traversal_queue) > 0:
        list_of_nodes = LinkedList()
        node = traversal_queue.popleft()
        if traversal_queue is None: # Store root in linked list [1] -> pop() -> []
            list_of_nodes.insert(node)

        else:
            list_of_nodes.insert(node)
            node2 = traversal_queue.popleft()
            list_of_nodes.insert(node2)
            if node2.left_child:
                traversal_queue.append(node2.left_child)
            if node2.right_child:
                traversal_queue.append(node2.right_child)




        if node.left_child:
            traversal_queue.append(node.left_child)
        if node.right_child:
            traversal_queue.append(node.right_child)
































