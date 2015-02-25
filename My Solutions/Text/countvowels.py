'''
Created For Mega Projects Repository

Problem: Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.

@author: Sambit

'''

word = raw_input("Enter a sentence \n").lower()
vowels = "aeiou"
count_total = 0
for i in vowels:
    count = word.count(i)
    print i,count
    count_total+=1

print "The total count of vowels is", count_total
