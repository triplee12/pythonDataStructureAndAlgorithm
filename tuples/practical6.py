__author__ = "Ejie Emmanuel Ebuka"

# Python tuple

myTuples = ("a", "b", "c", "d", "e", "f", "g")
print(f"Python tuple: {myTuples}")

# To create a single element in a tuple, you have to end the tuple with comma ","

myTuple = ("Dog",)
print(f"Single element: {myTuple}")

# Tuple operations and functions

# + operator: concatenate two tuple elements or more
myNumTuple = (1, 2, 3, 4, 5, 4, 4, 4, 5, 5, 4)
addition = myNumTuple + myTuples
print(f"+ operator: {addition}")

# * operator
print(myNumTuple * 5)

# in operator
print(4 in myNumTuple)

# count() function
print(myNumTuple.count(4)) # this will return the number of occurance

# index() function
print(myNumTuple.index(2)) # this will return the position of the first occurrence of an element

# len() function
print(len(myNumTuple))

# max() method
print(max(myNumTuple))

# min() method
print(min(myNumTuple))

# tuple() method
print(tuple([1, 2, 3, 4])) # this will return as a tuple
# By using tuple() method we can convert list to tuple.