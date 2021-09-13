__author__ = "Ejie Emmanuel Ebuka"

def fib(n):
    assert n >= 0 and int(n) == n, "Fib must a positive integer number."
    if n in [0, 1]:
        return n
    else:
        total = fib(n - 1) + fib(n - 2)
        print(total)
        return total

result = fib(20)
print(result)