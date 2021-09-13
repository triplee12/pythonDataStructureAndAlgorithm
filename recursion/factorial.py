__author__ = "Ejie Emmanuel Ebuka"


def factorial(n):
    assert n >= 0 and int(n) == n, "n must be positive integer only!"
    if n in [0,1]:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)

total = factorial(4)
print(f"Factorial of 4: {total}")