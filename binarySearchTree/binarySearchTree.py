__author__ = "Ejie Emmanuel Ebuka"

# Binary Search Tree

# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             rootNode = customQueue.dequeue()
#             print(root.value.data)
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild == nodeValue:
            print("The left child is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild == nodeValue:
            print("The right child is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

