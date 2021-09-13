__author__ = "Ejie Emmanuel Ebuka"

# Recursion Vs Iteration
# Recursion
def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n - 1)
        result = power * 2
        print(result)
        return result
print("Power of two using recursion method")
powerOfTwo(100)

# Iteration
def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i += 1
        print(power)
    return power
print("Power of two using iteration method")
powerOfTwoIt(100)

