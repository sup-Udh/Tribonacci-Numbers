# the challange 

#Write a python program to print the sequence where the number is the sum of previous three numbers. Start with 0 1 1. Example: 0 1 1 2 4 7 13 24 44 ... Here 2 is (0 + 1 + 1), 4 is ( 1 + 1 + 2) etc. *


# A simple recursive CPP program to print
# first n Tribonacci numbers.
 
def printTribRec(n) :
    if (n == 0 or n == 1 or n == 2) :
        return 0
    elif (n == 3) :
        return 1
    else :
        return (printTribRec(n - 1) +
                printTribRec(n - 2) +
                printTribRec(n - 3))
         
 
def printTrib(n) :
    for i in range(1, n) :
        print( printTribRec(i) , " ", end = "")
         
 
# Driver code
n = 10
printTrib(n)
 

 