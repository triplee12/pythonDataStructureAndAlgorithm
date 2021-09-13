__author__ = "Ejie Emmanuel Ebuka"

# List operations and functions

# + operator: concatenate lists
first_list = [1, 2, 3, 4, 5]
second_list = [1, 2, 3, 4, 5]

add_together = first_list + second_list
print(add_together)

# * operator
multiply = first_list * 5
print(multiply)

# Calculate the length of the list using len() function
length = len(first_list)
print(length)

# Get the maximum item in a list using max() function.
maximum = max(first_list)
print(maximum)

# Get minimum item in a list using min() function
minimum = min(first_list)
print(minimum)

# Calculate the sum all items in a list using sum() function.
total = sum(first_list)
print(total)

# From the functions discussed above, we can find the average of the list
print(sum(second_list) / len(second_list))