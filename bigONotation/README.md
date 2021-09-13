# Big O Notation

Big O is the language and metric we use to describe the efficiency of algorithms.

- Best case - O(N)
- Average case - O(N log N)
- Worst case - O(N^2)

## Big O, Big Theta and Big Omega

- Big O: It is a complexity that is going to be less or equal to the worst case. Big O - O(N)

- Big Omega: It is a complexity that is going to be at least more than the best case. Big OM - OM(1)

- Big Theta: It is a complexity that is within the worst case and the best cases. Big Theta - Theta(n/2)

## algorithm run time complexities

O(1) - Constant: Accessing a specific element in array. Example
array = [1,2,3,4,5,6]
array[0] # It takes constant time to access first element in array.

O(N) - Linear: Loop through array elements. Example:
array = [1,2,3,4,5,6]
for element in array:
    print(element) # Linear time since it is visiting every element of array.

O(LogN) - Logarithmic: Find an element in sorted array. Example:
array = [1,2,3,4,5,6]
for index in range(0, len(array), 3):
    print(array[index]) # logarithmic time since it is visiting only some elements

O(N^2) - Quadratic: Looking at a every index in array twice. Example:
array = [1,2,3,4,5,6]
for x in array:
    for y in array:
        print(x, y)

O(2^N) - Exponential: Double recursion in Fibonacci. Example:
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

## Space complexity

## Why do we drop constants and non dominant terms?

- It is very possible that O(N) code is faster than O(1) code for specific inputs.

- Different computers with different architectures have different constant factors.

- Different algorithms with the same basic idea and computational complexity might have slightly different constants.

Example:
a*(b-c) vs a*b-a*c

- As n approaches infinity, constant factors are not really a big deal.

## Add vs Multiply

- If your algorithm is in the form "do this, then when you are all done, do that" then you add the runtimes.

- If your algorithm is in the form "do this for each time you do that" then you multiply the runtimes.

## How to measure the codes using Big O?

- Rule 1: Any assignment statements and if statements that are executed once regardless of the size of the problem. O(1)

- Rule 2: A simple "for" loop from 0 to n (with no internal loops) O(n)

- Rule 3: A nested loop of the same type takes quadratic time complexity O(n^2)

- Rule 4: A loop in which the controlling parameter is divided by two at each step O(log n)

- Rule 5: When dealing with multiple statements, just add them up

### Interview Questions

Please use comment box on github.com to answer questions below.

- What is a data structure?

- What is an algorithm?

- Big O?

- Recursion?
