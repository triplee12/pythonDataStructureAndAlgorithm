__author__ = "Ejie Emmanuel Ebuka"

# Linked List

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insertLinkList(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

sLinkedList: SingleLinkedList
sLinkedList = SingleLinkedList()
sLinkedList.insertLinkList(1, 1)
sLinkedList.insertLinkList(2, 1)
sLinkedList.insertLinkList(3, 1)
sLinkedList.insertLinkList(4, 1)
sLinkedList.insertLinkList(5, 1)
sLinkedList.insertLinkList(6, 1)
sLinkedList.insertLinkList(7, 1)
sLinkedList.insertLinkList(8, 1)
sLinkedList.insertLinkList(9, 1)

print([node.value for node in sLinkedList])

sLinkedList.insertLinkList(1, 2)
sLinkedList.insertLinkList(2, 2)
sLinkedList.insertLinkList(3, 2)
sLinkedList.insertLinkList(4, 2)
sLinkedList.insertLinkList(5, 2)
sLinkedList.insertLinkList(6, 2)
sLinkedList.insertLinkList(7, 2)
sLinkedList.insertLinkList(8, 2)
sLinkedList.insertLinkList(9, 2)

print([node.value for node in sLinkedList])