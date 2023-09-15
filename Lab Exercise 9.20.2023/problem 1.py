##Lab Exercise 9/20/2023 Problem 1
##Author: nmessa
##This program generates a list of 1000 elements
##The list contains random integers ranging from 1 to 10000
import random

#create an empty list
numbers = []

#generate list
for _ in range(1000):
    numbers.append(random.randint(1, 10000))

#this code will print the list in 10 columns
for i in range(len(numbers)):
    print(numbers[i], end = '  ')
    if i % 10 == 0:
        print()




