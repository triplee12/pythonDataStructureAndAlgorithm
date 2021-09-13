__author__ = "Ejie Emmanuel Ebuka"

# Store user input in a list

user_list = list()
print("Enter 'done' to exit the program")
while (True):
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    value = float(user_input)
    user_list.append(value)
    total = sum(user_list)
    length = len(user_list)
    average = total / length
print(f"Average: {average}")
print(f"Numbers in your list are: {user_list}")