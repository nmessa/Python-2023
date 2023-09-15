##Lab Exercise 9/18/2023 Problem 1
##Author: nmessa
##Find the smallest of 3 numbers

#This function returns the smallest value of the 3 parameters passed to it
def smallest(x, y, z):
    if x <= y and x <= z:
        return x
    if y <= x and y <= z:
        return y
    if z <= y and z <= x:
        return z

#Test code
print (smallest(1, -2, 3))
print (smallest(2, 1, 3))
print (smallest(3, 2, 1))

