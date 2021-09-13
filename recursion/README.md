# What is Recursion

Recursion is a way of solving a problem by having a function calling itself.
Example - Russia frsction ball.

- Performing the same operation multiple times with different inputs.

- In every step we try smaller inputs to make the problem smaller.

- Base condition is needed to stop the recursion, otherwise infinite recursion / loop will occur.


## Why Recursion?

1. Recursive thinking is really important in programming and it helps us brak down big problems into smaller ones and easier to use.

### When to use recursion

- If you can divide the problem into similar sub problems.

- Design an algorithm to compute nth...

- Write code to list the n...

- Implement a method to compute all.

- Practice

2. The prominent usage of recursion in data structures like trees and graphs.

3. Interviews

4. It is used in many algorithms (divide and conquer, greedy and dynamic programming)


## How Recursion works?

1. A method calls it self
2. Exit from infinite loop

## When to use recursion?

- When we can easily breakdown a problem into similar subproblems
- When we are fine with extra overhead (both time and space) that comes with it

- When we need a quick working solution instead of efficient one.

- When traverse a tree
- When we use memoization in recursion

## When to avoid recursion?

- If time and space complexity matters for us.
- Recursion uses more memory. if we use embededded memory. For example an application that takes more memory in the phone is not efficient.

- Recursion can be slow


## How to write recursion in 3 steps?

1. Factorial

- It is the product of all positive integers less than or equal to n.

- Denoted by n! (Christian Kramp in 1808).

- Only positive numbers.

- 0! = 1.

Example 1
4! = 4*3*2*1 = 24

Example 2
10! = 10*9*8*7*6*5*4*3*2*1 = 3628800

n! = n*(n-1)*(n-2)*...*2*1

### Step 1: Recursive case - the flow

n! = n*(n-1)*(n-2)*...*2*1

### Step 2: Base case - the stopping criterion

0! = 1
1! = 1

### Step 3: Unintentional case - the constraint

## Fibonacci numbers - Recursion

Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones and the sequence starts from 0 and 1
