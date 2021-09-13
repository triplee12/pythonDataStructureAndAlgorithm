__author__ = "Ejie Emmanuel Ebuka"

# Find average of user input using standard average formula

total = 0
count = 0
print("Enter 'done' to exit the program")
while (True):
    user_input = input("Enter a number ")
    if user_input == "done":
        break
    value = float(user_input)
    total = total + value
    count = count + 1
    average = total / count
print(f"Average: {average}")