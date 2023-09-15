## Lab Exercise 9/19/2023 Problem 9
## Author: nmessa
## This program prints the contents of 2 lists.  Lists are same length

#Define the lists
list1 = [10,20,30,40]
list2 = [100, 200, 300, 400]

#Print contents of the 2 lists alternating lists
for i in range(len(list1)):
    print(list1[i], list2[len(list2)-1-i])

#Output
##10 400
##20 300
##30 200
##40 100
