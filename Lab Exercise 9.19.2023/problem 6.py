## Lab Exercise 9/19/2023 Problem 6
## Author: nmessa
## This program concatenates 2 lists.  Both list have same length

#Define the lists
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
output = []

#Concatenate the lists
for i in range(len(list1)):
    word = list1[i] + list2[i]
    output.append(word)

#Print the list
print(output)

#Output
#['My', 'name', 'is', 'Kelly']
