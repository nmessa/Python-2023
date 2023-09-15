##Lab Exercise 9.21.2023 Problem 4
##Author: nmessa

from random import randint

#This function finx max, min, and mean of data
def listStats(nums):
    maximum = max(nums)
    minimum = min(nums)
    mean = sum(nums)/len(nums)
    return maximum, minimum, mean

#Create list of 1000 elements ranging from 1 to 10000
numbers = []
for i in range(1000):
    numbers.append(randint(1, 10000))

#Call listStats
maximum, minimum, mean = listStats(numbers)

#print results
print("Maximum value =", maximum)
print("Minimum value =", minimum)
print("Mean value =", mean)

##Sample Output
##Maximum value = 9932
##Minimum value = 14
##Mean value = 5054.164
