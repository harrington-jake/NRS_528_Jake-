#1. List Values

#Make a new list that has all the elements less than 5 from this list (li below) in it and print out this new list.
#Write this in one line of Python (you do not need to append to a list just print the output).
li = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]

# First I'll Create a blank list called new_list:
new_list = []

# Now I will use a for loop to look at every item in list li, and if the list item is <5, it will add that
# item into new_list.
for i in li:
    if i < 5:
        new_list.append(i)
print(new_list)

#Now to do the same thing in one line.
# Got help from https://stackoverflow.com/questions/32580489/python-for-and-if-on-one-line
print([i for i in li if i <= 5])
