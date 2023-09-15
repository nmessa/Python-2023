## Lab Exercise 9/19/2023 Problem 2
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

#Sort the list
names.sort()
#print the list
print("The sorted list is: ")
for i in range(len(names)):
    print (names[i], end = ' ')
print()

##Output
##Enter name: Jack
##Enter name: Mary
##Enter name: Alice
##Enter name: Joe
##Enter name: Fred
##The list now contains: 
##Jack Mary Alice Joe Fred 
##The sorted list is: 
##Alice Fred Jack Joe Mary 







