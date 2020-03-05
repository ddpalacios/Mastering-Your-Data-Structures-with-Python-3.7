class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


root = Node(3)
n2 = Node(5)
n3 = Node(1)
n4 = Node(6)
n5 = Node(2)
n6 = Node(7)
n7 = Node(4)
n8 = Node(0)
n9 = Node(8)


root.left_child = n2
root.right_child = n3

n2.left_child = n4
n2.right_child = n5


n5.left_child = n6
n5.right_child = n7

n3.left_child = n8
n3.right_child = n9

# current = root
# while current:
#     print(current.data)
#     current = current.right_child
#
# print("\n")


def preorder(root_node):
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


def postorder(root_node):
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)


print(inorder(root.left_child))