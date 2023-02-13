#3. Given a singe phrase, count the occurrence of each word

# Using this string:
#
string = 'hi dee hi how are you mr dee'
# Count the occurrence of each word, and print the word plus the count
# (hint, you might want to "split" this into a list by a white space: " ").

# Thanks to the hint, I used the split function to turn every word the in the string into a list item.
now_list = string.split()
print(now_list)

#Below I run a loop that uses the count function to count the number of occurrences of each item in the list.
#Then I print each list item with it's count.
for i in now_list:
    print(i + ' - ' + str(now_list.count(i)))
