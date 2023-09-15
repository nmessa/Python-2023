## Lab Exercise 9/19/2023 Problem 4
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

#replace one of the names in the list using remove and insert methods
choice = int(input('Replace one name.  Which one? (1 - 5)'))
replace = names[choice-1]
newName = input("New name: ")
names.remove(replace)
names.insert(choice-1, newName)

#print the list
for i in range(len(names)):
    print (names[i], end = ' ')
print()

##Output
##Enter name: Mary
##Enter name: Fred
##Enter name: Joe
##Enter name: Anne
##Enter name: Jack
##The list now contains: 
##Mary Fred Joe Anne Jack 
##Replace one name.  Which one? (1 - 5)2
##New name: Mack
##Mary Mack Joe Anne Jack 





