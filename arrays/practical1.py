__author__ = "Ejie Emmanuel Ebuka"

from array import *

# Create an array

myNum = array("i", [1,2,3,5,7,6,8,0,9])

for i in myNum: # Traverse
    print(i)

# Access individual elements through indexes
print(f"Index {myNum[0]}")

# Append any element at any end ofan array using append() method
myNum.append(20)
print(myNum)

# Insert element in an array using insert() method
# Insert at any given index
myNum.insert(2, 15)
print(myNum)

# Using extend() method to add element in an array
myNum_2 = array("i", [100, 200, 500])
myNum.extend(myNum_2)
print(myNum)

# Using fromlist() method to add items in an array
myList = [5, 10, 15, 20]
myNum.fromlist(myList)
print(myNum)

# Using remove() to remove element from an array
myNum.remove(0)
print(myNum)

# Using pop() method to remove element from an array
myNum.pop(6)
print(myNum)

# Fetching element using index() method
print(myNum.index(1))

# Using reverse() method to reverse any given array
myNum.reverse()
print(myNum)

# Using buffer_info() method to get array buffer information
buffer = myNum.buffer_info()
print(buffer)

# Using count() method to count how many occurance an element occurs in an array
occur = myNum.count(5)
print(occur)

# Convert an array to string using tostring() method
fromArray = myNum.tostring()
print(fromArray)
# To confirm our conversion
myInts = array("i")
myInts.fromstring(fromArray)
print(myInts)

# Convert an array to list using tolist() method
print(myNum.tolist())

# Slice elements in an array
print(myNum[1:10]) # This will print element from index 1 to index 10.
