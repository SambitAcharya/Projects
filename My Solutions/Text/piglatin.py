'''

Created For Mega Projects Repository

Problem: Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed
(Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

@author: Sambit

'''

sentence = raw_input("Enter a sentence \n")

for word in sentence.split():
    if word[0] in "aeiou":
        print word + "way"
    else:
        print word[1:] + "-" + word[0] + "ay"
