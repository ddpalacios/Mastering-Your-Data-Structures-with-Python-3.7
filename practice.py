

class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None



class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = SinglyNode(data)
        if self.head:
            self.head.next = new_node
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
        self.size +=1


    def remove(self, data):
        prev = self.tail
        current = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -=1
                return

            prev = current
            current = current.next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def append(self, data):
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size +=1


    def remove(self, data):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = self.head.next
            self.head.prev = None
            node_deleted = True

        elif self.tail == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.size -=1

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node

        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if new_node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = new_node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = new_node
                        return


if __name__ == '__main__':
    print("BST:")
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(0)
    root = tree.root
    print(root.data, root.left_child.data, root.left_child.left_child.data)


    print("Doubly Linked List:")
    doubly = DoublyLinkedList()
    doubly.append(1)
    doubly.append(2)
    doubly.append(3)
    doubly.append(4)
    head = doubly.head
    print(head.data, head.next.data, head.next.prev.data)
    doubly.remove(2)
    print(head.data, head.next.data, head.next.prev.data)


    print("Singly Linked list")
    linkedlist = SinglyLinkedList()
    linkedlist.append(4)
    linkedlist.append(1)
    linkedlist.append(9)
    linkedlist.append(2)
    linkedlist.append(4)
    linkedlist.append(2)
    tail = linkedlist.tail

    linkedlist.remove(9)


    print("LIST SIZE:", linkedlist.size)
    while tail:
        print(tail.data)
        tail = tail.next

