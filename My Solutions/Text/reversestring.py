'''
Created For Mega Projects Repository

@author: Sambit

'''

def reverse(string):
    """

        @param Input: Given String
        @return Output: Reversed String

    """
    return string[::-1]

#Storing the input in @variable string
string = input("Enter the string \n")

#Printing the output to the console.
print("The reversed string is \n"+reverse(string))
