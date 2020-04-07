# '''
#
# a Binary search tree (BST) is a special kind of binart tree and it is
# one of the most important and commonly used data structures in computer
# science applications.
#
#
# A BST is a tree that is structually a binary tree, and stores data in its nodes very efficiently.
# It provides very fast SEARCH operations and other operations like: INSERTION AND DELETION
#
#
# A binary tree is called a bst:
#
# IF value at any node is >= valyes in all the nodes of its left sub-tree and less than or equal to the values
# of all the nodes of the right sub-tree.
#
# '''
#
#
# # of course, we create our Node class with its attributes of left and right child
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left_child = None
#         self.right_child = None
#
#
# # To start we will need to keep track of the root node
# # Lets make a Tree class that holds that refrence to the root node
# class Tree:
#     def __init__(self):
#         self.root_node = None  # That is all that is needed
#
#     # Lets examine the main operations on the tree (Insert, delete, finding min/max/searching)
#     # First, finding the min and max node of the tree (path for min: LEFT CHILD
#     #                                                  path for max: RIGHT CHILD)
#
#     def find_min(self):
#         current = self.root_node
#         while current.left_child:
#             current = current.left_child  # This is just our standard pointer iteration
#         return current  # after there are no more left childeren, we found the min and return it
#
#     # Now lets do the same for the max (except for the right child)
#     def find_max(self):
#         current = self.root_node
#         while current.right_child:
#             current = current.right_child  # Keep iterating our path of the right child
#         return current
#
#     # One the most important operations to implement is to insert data items in the tree
#     # We have to keep in mind that BST have a certain criteria of how BST nodes are stored
#     # A quick run through:
#     '''
#     The left child nodes should contain the data less than their own value and the right
#     child should have data greater than their value
#     So we have to ensure that the property if the BST satisfies whenever we insert an item
#     in the tree.
#     '''
#     def insert(self, data):
#         node = Node(data)
#         if self.root_node is None:  # First check if we have a root
#             self.root_node = node
#         else:
#             # We need to keep track of the curr node. as well as the parent.
#             # We use a current variable to be used for that purpose
#             current = self.root_node
#             parent = None
#             while True:
#                 parent = current
#
#                 # from here, we need to perform comparisons in order to maintain
#                 # a proper binary search tree
#                 if node.data < current.data:
#                     current = current.left_child
#                     if current is None:
#                         parent.left_child = node
#                         return
#
#                 # Now we have to take care of the greater than or equal case.
#                 # if the current node does not have a right child then the new node
#                 # is inserted as the right child node. Otherwise we move down and continue
#                     if current is None:
#                         parent.right_child = node
#                         return
#                 # looking for an insertion point
#                 else:
#                     current = current.right_child
#
#                 # Insertion takes O(h) where h is the height of the tree
#
#                 # Now we are going to look at deletion of nodes
#                 # There are three scenarios for what the node might have:
#                 '''
#                 1) No Children -> directly remove it
#                 2) One Child -> Swap value of that node with its child, and then delete the node
#                 3) Two children -> We find the in-order successor or predecessor, swap the val with it and delete that node
#
#                 So lets take a look on how we can handle these scenarios in code
#                 '''
#     # Since our node class does not have a reference to a parent. We need a helper method to search and return the node
#     # with its parent node
#     def get_node_with_parent(self, data):
#         parent = None
#         current = self.root_node
#         if current is None:
#             return parent, None
#
#         while True:
#             if current.data == data:
#                 return parent, current
#
#             elif current.data > data:
#                 parent = current
#                 current = current.left_child
#             else:
#                 parent = current
#                 current = current.right_child
#
#         return parent, current
#
#
#     def remove(self, data):
#         parent, node = self.get_node_with_parent(data)
#         if parent is None and node is None:
#             return False
#         # Get childrent count for each scenerio
#         childeren_count = 0
#
#         # it is important to know the # of childrent that the node has
#         # in order to delete it properly
#
#         if node.left_child and node.right_child:
#             childeren_count = 2
#         elif node.left_child is None and node.right_child is None:
#             childeren_count = 0
#         else:
#             childeren_count = 1
#
#         # Once we do know the number of children, we conduct our if statements
#         if childeren_count == 0:
#             if parent:
#                 if parent.right_child is node:
#                     parent.right_child = None
#                 else:
#                     parent.left_child = None
#             else:
#                 self.root_node = None
#
#         # Next scenerio
#         elif childeren_count == 1:
#             next_node = None
#             if node.left_child:
#                 next_node = node.left_child
#             else:
#                 next_node = node.right_child
#             if parent:
#                 if parent.left_child is node:
#                     parent.left_child = next_node
#                 else:
#                     parent.right_child = next_node
#             else:
#                 self.root_node = next_node
#
#         # For two children ...
#         parent_of_leftmost_node = node
#         leftmost_node = node.right_child
#         while leftmost_node.left_child:
#             parent_of_leftmost_node = leftmost_node
#             leftmost_node = leftmost_node.left_child
#
#         node.data = leftmost_node.data
#
#     # Now lets implement a method for searching for a specific node
#     # its pretty simple to follow
#     def search(self, data):
#         current = self.root_node
#         while True:
#             if current is None:
#                 return None
#             elif current.data is data:
#                 return data
#
#             elif current.data > data:
#                 current = current.left_child
#             else:
#                 current = current.right_child
#
#
#     '''
#     Summary:
#     Linked list are efficient for insertion and deletion
#     BUT SLOW FOR SEARCHING O(N)
#
#     BST are efficient for searching, insertion, and deletion
#     Best case is O(log n)
#     Worsr: O(n)
#     '''
#
# # Lets finallt write some code to insert nodes in our tree
# tree = Tree()
# tree.insert(5)
# tree.insert(10)
# tree.insert(80)
# tree.insert(7)
# tree.insert(3)
# tree.insert(2)
# tree.insert(4)
# root = tree.root_node
#
#
#
# for i in range(1, 10):
#     found = tree.search(i)
#     print("{}: {}".format(i, found))
#
#
#
# print("MAX: {}\nMIN: {}\n".format(tree.find_max().data, tree.find_min().data))
#
class Node:
    def __init__(self, data):
        self.data =data
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node

        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return
from time import sleep
def check(root):
    parent_val = root.data
    l_val, r_val = root.left_child, root.right_child

    if l_val is None and r_val is None:
        print(parent_val, 'is end')
        sleep(2)
        return

    elif l_val is None:
        if r_val.data > parent_val:
            print(parent_val, "is a BST")
            sleep(2)
            check(root.right_child)

    elif r_val is None:
        if l_val.data < parent_val:
            print(parent_val.data, 'is a BST')
            sleep(2)

            check(root.left_child)


    elif l_val.data <= parent_val and r_val.data > parent_val:
        print(parent_val, "is a BST")
        sleep(2)
        print("feeding", root.left_child.data)
        check(root.left_child)
        print("feeding", root.right_child.data)
        check(root.right_child)
        return True
    else:
        print("NOT A BST")
        return False








tree = BinaryTree()
tree.insert(10)
tree.insert(1)
tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(12)
tree.insert(8)
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(11)
tree.insert(15)
tree.insert(0)

root = tree.root

print(check(root))
# cl
# preorder(root)ass LinkedNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.tail = None
#         self.head = None
#
#     def append(self, data):
#         node = LinkedNode(data)
#         if self.head:
#             self.head.next = node
#             self.head = node
#         else:
#             self.tail = node
#             self.head = node
#
#
# from collections import deque
# def breadth_first_search(node, linkedlist):
#     if node.left_child and node.right_child:
#         print("Linked list appended: ", node.left_child.data)
#         print("Linked list appended: ", node.right_child.data)
#         linkedlist.append(node.left_child.data)
#         linkedlist.append(node.right_child.data)
#
# def preorder(root, depth=0):
#     current = root
#     linkedlist = SinglyLinkedList()
#     if current is None:
#         print("end".upper())
#         return
#     print("Checking Depth:", depth, "DATA:",current.data)
#     if depth == 0:
#         root = current
#         linkedlist = SinglyLinkedList()
#         print("ROOT Linked list made and appended: ", root.data)
#         linkedlist.append(root.data)
#     linkedlist = SinglyLinkedList()
#     print("Linked list made")
#     breadth_first_search(root, linkedlist)
#     preorder(current.left_child, depth+1)
#     preorder(current.right_child, depth +1)
#

# linkedlist = SinglyLinkedList()
# linkedlist.append(1)
# linkedlist.append(12)
# linkedlist.append(13)
# linkedlist.append(14)
# linkedlist.append(14)
# linkedlist.append(14)
#
#
# tail = linkedlist.tail
# while tail:
#     print(tail.data)
#     tail = tail.next

# print(tail.next.data, tail.next.next.data)