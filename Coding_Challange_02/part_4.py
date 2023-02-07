# 4. User input
# Ask the user for an input of their current age, and tell them how many years until they reach
# retirement (65 years old).
#
# Hint:
#
# age = input("What is your age? ")
# print "Your age is " + str(age)

#Ask the user for a number input and save it an integer in the variable 'age'.
age=int(input('How old are you? (enter number): '))

#Create a variable that is the number between the number input and retirement age(65)
toret=65-age

#I decided to get a little fancy and create an if statement where if the input age is less than 65, it prints the number
#of years until they reach 65. But if the input number is 65 or greater, the output says the user has already
# reached retirement age
if age < 65:
    print('You have ' + str(toret) + ' years until retirement.')
else:
    print('You have already reached retirement age!')
