__author__ = "Ejie Emmanuel Ebuka"

# Python dictionary operations and built in functions

myName = {"firstName":"Ebuka", "lastName":"Emmanuel", "surName":"Ejie"}

# in operator; checks if an item in the dictionary exists, returns True if it exists and False otherwise
print("firstName" in myName) # This will return True otherwise False if not found

# for operator
for k, v in myName.items():
    print("{}={}".format(k, v)) # This will return Keys and Values of myName

# all() method will return True if all keys in the dictionary are found, otherwise False
# syntax: all(dictionary)
# if all values are False it returns False, if one is True it returns False
# if one value is False it returns False and if it is empty it returns True
allTrue = {1: True, 2: True, 3: True, 4: True}
print("all() method")
print(f"All True values: {all(allTrue)}")
allFalse = {1: False, 2: False, 3:False}
print(f"All False values: {all(allFalse)}")
someTrue = {1:True, 2: True, 3:False}
print(f"Some True values: {all(someTrue)}")
someFalse = {1:False, 2: False, 3:True}
print(f"Some False values: {all(someFalse)}")
emptyDict = {}
print(f"Empty dict: {all(emptyDict)}")

# any() method will return True if any or all value(s) is True and False otherwise
print("any() method")
print(f"Any value: {any(someTrue)}")
print(f"All False values: {any(someFalse)}")
print(f"All True values: {any(allTrue)}")
print(f"All False values: {any(allFalse)}")
print(f"Empty dict: {any(emptyDict)}")

# len() method returns the number of items in the dictionary
print("len() method")
print(f"The length of the allTrue values: {len(allTrue)}")

# sorted() method returns the sorted items of dictionary
# sorted() method takes three arguments: iterable, reverse, and key
print(f"The sorted items of dictionary: {sorted(allTrue, reverse=True)}")