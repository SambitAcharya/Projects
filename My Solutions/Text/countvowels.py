word = raw_input("Enter a sentence \n").lower()
vowels = "aeiou"
count_total = 0
for i in vowels:
    count = word.count(i)
    print i,count
    count_total+=1

print "The total count of vowels is", count_total
