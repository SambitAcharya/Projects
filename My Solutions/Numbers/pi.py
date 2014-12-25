'''
Created For Mega Projects Repository

Problem: Find PI to the Nth Digit
Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.

@author: Sambit

'''

#Imports
from decimal import *

#Function to calculate the value of PI using Bellard's algorithm
def bellard(n):
    """

        @param Input: Number of digits after the decimal point.
        @return Output: Value of PI with precision upto @param digits

    """
    pi = Decimal(0)
    k = 0
    while k<n:
        pi += (Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) -Decimal(1)/(4*k+3))
        k += 1
    pi = pi * 1/(2**6)

    return pi

#Storing the input in @variable string
NUMBER_OF_DIGITS = int(input("Enter the number of digits \n"))

'''
Number of digits have to be greater than zero
Value set to 2 if any such input is given.
'''

if NUMBER_OF_DIGITS <= 0:
    print("Number Of Digits set as negative or zero.")
    print("Number Of Digits set to 2")
    NUMBER_OF_DIGITS = 2

getcontext().prec = NUMBER_OF_DIGITS + 1
VALUE_OF_PI = bellard(NUMBER_OF_DIGITS + 1)

#Printing the output to the console.
print(VALUE_OF_PI)
