## Lab Exercise 9/19/2023 Problem 1
## Author: nmessa
## This program demonstrates the use of lists

#Create empty list
names = []

#Create list with 5 names
for i in range(5):
    name = input("Enter name: ")
    names.append(name)

#print the list
print("The list now contains: ")
for i in range(len(names)):
    print (names[i], end = ' ')
print()

##Output
##Enter name: Fred
##Enter name: Mary
##Enter name: Jane
##Enter name: Alex
##Enter name: Martin
##The list now contains: 
##Fred Mary Jane Alex Martin 





