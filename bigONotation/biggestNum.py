__author__ = "Ejie Emmanuel Ebuka"


numArray = [1,2,3,7,9,100,288,17, 48,8,4,200,50,1000,2,6,8,9,556,778,97,443,788,1234,7899,94,678,943,2435]

def findBiggestNumber(numArray):
    biggestNumber = numArray[0]
    for index in range(1, len(numArray)):
        if numArray[index] > biggestNumber:
            biggestNumber = numArray[index]
    print(f"Biggest number is {biggestNumber}")

findBiggestNumber(numArray)