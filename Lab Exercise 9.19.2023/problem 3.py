## Lab Exercise 9/19/2023 Problem 3
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

#print the third element
print ("The third element is", names[2])
print()

##Output
##Enter name: Mary
##Enter name: Jack
##Enter name: Fred
##Enter name: Wilma
##Enter name: Betty
##The list now contains: 
##Mary Jack Fred Wilma Betty 
##The third element is Fred






