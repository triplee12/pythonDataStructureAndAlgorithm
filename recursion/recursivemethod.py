__author__ = "Ejie Emmanuel Ebuka"

def recursivemethod(n):
    if n < 1:
        print(f"n is less than 1: n is {n}")
    else:
        recursivemethod(n - 1) # recursive
        print(f"n is greater than 1: n is {n}")

recursivemethod(100) # recursive method, calling recursive method 101 times starting from 0 to 100