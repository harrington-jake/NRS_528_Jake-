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

#Creates a new dictionary where each letter is the key for it's score.
my_scores = {letter: score
                 for letters, score in letter_scores.items() for letter in letters}

#saves the user input word as a variable called 'word'
word = input('enter a word: ')

#Prints the sum of values associated with the letter of each letter in the user input word.
print(sum(my_scores[letter] for letter in word.lower()))


