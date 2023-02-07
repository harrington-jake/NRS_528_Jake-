# 2. List overlap
# Using these lists:

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
# Determine which items are present in both lists.
# Determine which items do not overlap in the lists.

# First I create a blank list:
overlap = []

#Now i will loop through the two lists, and every time an item appears in both lists,
# it will be added to the 'overlap' list.
for i in list_a:
    for z in list_b:
        if i == z:
            overlap.append(i)
print(overlap)



# Finding items that don't overlap stumped me, so I found help at https://stackoverflow.com/questions/40185258/find-elements-not-in-the-intersection-of-two-lists

# My idea was to create a list containing all items, then remove the items present in the overlap list.
#It turns out I needed to convert my lists using the set function to do this.
#The capital S in the variable names indicates that they have been converted to sets.

#This line combines the 2 lists.
list_both = list_a + list_b

#These lines convert the lists to sets, removes the items in 'overlap' from 'list_both' and prints the remianing items.
list_bothS = set(list_both)
overlapS = set(overlap)
print(list_bothS - overlapS)

