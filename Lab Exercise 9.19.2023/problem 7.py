## Lab Exercise 9/19/2023 Problem 7
## Author: nmessa
## This program squares each element in a list

#Define the list
myList = [1,2,3,4,5,6,7]


#Square each element of the list
for i in range(len(myList)):
    myList[i] = myList[i] ** 2
    

#Print the list
print(myList)

#Output
#[1, 4, 9, 16, 25, 36, 49]
