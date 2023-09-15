##Lab Exercise 9/18/2023 Problem 4
##Author: nmessa
##finds the middle of a string

#This function will return the middle character in a string
#If the string has an odd number of characters it will return 1 char
#If the string has an even number of characters it will return 2 chars
def middle(string):
    if len(string) % 2 != 0: #odd
        return string[len(string)//2]
    else:
        return string[(len(string)//2)-1] + string[len(string)//2] 
    

#Test code
print (middle('transit')) #n
print (middle('cheesecake')) #se



