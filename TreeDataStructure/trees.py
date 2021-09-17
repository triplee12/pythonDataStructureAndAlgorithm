__author__ = "Ejie Emmanuel Ebuka"

# Tree Data Structure

class Tree:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, Tree):
        self.children.append(Tree)

tree = Tree("Drinks", [])
cold = Tree("Cold", [])
hot = Tree("Hot", [])

tea = Tree("Tea", [])
coffee = Tree("Coffee", [])

beer = Tree("Beer", [])
wine = Tree("Wine", [])
cola = Tree("Cola", [])
fanta = Tree("Fanta", [])

tree.addChild(cold)
tree.addChild(hot)

hot.addChild(tea)
hot.addChild(coffee)

cold.addChild(beer)
cold.addChild(wine)
cold.addChild(cola)
cold.addChild(fanta)

print(tree)