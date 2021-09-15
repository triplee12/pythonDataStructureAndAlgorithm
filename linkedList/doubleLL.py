__author__ = "Ejie Emmanuel Ebuka"

# Double Linked List

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def create(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "Double Linked List is created successfully."


doubleLinkedList: DoubleLL
doubleLinkedList = DoubleLL()

doubleLinkedList.create(0)

print([node.value for node in doubleLinkedList])