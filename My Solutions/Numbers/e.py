'''
Created For Mega Projects Repository

Find e to the Nth Digit - Just like the previous problem, but with e instead of PI.
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go.

@author: Sambit

'''
#Imports
from decimal import *

#Functions
def fact(n):

    '''

        @param Input: Number of whose the factorial is to be found.
        @return Output: Factorial of the given number

    '''

    fact = 1
    for i in range(1,n+1):
        fact*=i

    return fact

def determineValue(n):

    '''

        @param Input: Number of digits after the decimal point.
        @return Output: Value of E with precision upto @param digits

    '''

    val = Decimal(0)
    i = 0
    while i<=n:
        val+=Decimal(1)/Decimal(fact(i))
        i+=1
    return val

def main():

    #Storing the input in @variable string
    NUMBER_OF_DIGITS = int(input("Enter the number of digits \n"))

    '''

    Number of digits have to be greater than zero
    Value set to 2 if any such input is given.

    '''


    if NUMBER_OF_DIGITS <= 1:

        print("Number Of Digits set less than one. Unacceptable")
        print("Number Of Digits set to 2")
        NUMBER_OF_DIGITS = 2

    getcontext().prec = NUMBER_OF_DIGITS + 1
    VALUE_OF_E = determineValue(NUMBER_OF_DIGITS + 1)

    #Printing the output to the console.
    print(VALUE_OF_E)


main()
