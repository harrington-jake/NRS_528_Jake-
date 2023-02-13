# 2. Push sys.argv to the limit
# Construct a rudimentary Python script that takes a series of inputs as a command from a bat file using sys.argv, and does something to them. The rules:
#
# Minimum of three arguments to be used.
# You must do something simple in 15 lines or less within the Python file.
# Print or file generated output should be produced.

import sys

#First I'll print the 3 inputs from the .bat file I'm using.
print("Word 1: " + str(sys.argv[1]))
print("Word 2: " + str(sys.argv[2]))
print("Word 3: " + str(sys.argv[3]))

#I have decided to repilicate the scrabble problem from Coding Challange 2
#This time I will output the score of each of the 3 inputs in the .bat file.

#I'll organize my directory the same way I did in coding challange 2
letter_scores = {"aeioulnrst": 1,"dg": 2,"bcmp": 3,"fhvwy": 4,"k": 5,"jx": 8,"qz": 10}
my_scores = {letter: score
                 for letters, score in letter_scores.items() for letter in letters}

#1st I'll save each of the inputs as variable called word#
word1 = str(sys.argv[1])
word2 = str(sys.argv[2])
word3 = str(sys.argv[3])

# In the final 12 lines I calcualte then print the scrabble score for each of the words in the .bat file: 
word_score1 = 0
for letter in word1.lower():
    word_score1 += my_scores[letter]
print('The Scrabble score for "' + word1 + '" is ' + str(word_score1))

word_score2 = 0
for letter in word2.lower():
    word_score2 += my_scores[letter]
print('The Scrabble score for "' + word2 + '" is ' + str(word_score2))

word_score3 = 0
for letter in word3.lower():
    word_score3 += my_scores[letter]
print('The Scrabble score for "' + word3 + '" is ' + str(word_score3))



