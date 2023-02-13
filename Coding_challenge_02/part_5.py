# 5. User input 2
# Using the following dictionary (or a similar one you found on the internet), ask the user for a word,
# and compute the Scrabble word score for that word (Scrabble is a word game, where players make words from letters,
# each letter is worth a point value), steal this code from the internet, format it and make it work:

letter_scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}

#I couldn't figure it out using the given directory.
# So the code below creates a new dictionary where each letter is the key for it's score.
my_scores = {letter: score
                 for letters, score in letter_scores.items() for letter in letters}
print(my_scores)

#saves the user input word as a variable called 'word'
word = input('enter a word: ')

#Adds the point value of each letter in the user-input word to a variable called word_score (which starts at zero),
#Then prints a message teling the user their word's Scrabble score
#Used: https://www.codecademy.com/forum_questions/522f576fabf82117ec000f21 for help, but didn't bother making a function like they did.
word_score = 0
for letter in word.lower():
    word_score += my_scores[letter]
print('The Scrabble score for "' + word + '" is ' + str(word_score))

#Below is an alternative solution that I found online but didn't save the web adress and have been unable to find since.
#The single line of code below could replace lines 28-30 and produce the same result.
# word_score = (sum(my_scores[letter] for letter in word.lower()))


