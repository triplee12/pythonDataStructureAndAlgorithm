__author__ = "Ejie Emmanuel Ebuka"

numArray = [1,2,3,7,9,100,288,17, 48,8,4,200,50,1000,2,6,8,9,556,778,97,443,788,1234,7899,94,678,943,2435]

def findMaxNumRecursive(numArray, n):
    if n == 1:
        return numArray[0]
    return max(numArray[n - 1], findMaxNumRecursive(numArray, n - 1))

maxNum = findMaxNumRecursive(numArray, n=len(numArray))
print(maxNum)