'''
Created For Mega Projects Repository

Problem: Reverse a String - Enter a string and the program will reverse it and print it out.

@author: Sambit

'''
#Functions

#Function to compute the reverse of the string
def reverse(string):

    """

        @param Input: Given String
        @return Output: Reversed String

    """
    return string[::-1]

#Main Function
def main():

    #Storing the input in @variable string
    string = input("Enter the string \n")

    #Printing the output to the console.
    print("The reversed string is \n"+reverse(string))

main()
