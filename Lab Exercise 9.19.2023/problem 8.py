## Lab Exercise 9/19/2023 Problem 8
## Author: nmessa
## This program prints the permutations of 2 lists

#Define the lists
list1 = ["Hello" , "take"]
list2 = ["Dear", "Sir"]
output = []

#Generate 4 permutations
output.append(list1[0] + " " + list2[0])
output.append(list1[0] + " " +  list2[1])
output.append(list1[1] + " " +  list2[0])
output.append(list1[1] + " " +  list2[1])
    

#Print the list
print(output)

#Output
#['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
