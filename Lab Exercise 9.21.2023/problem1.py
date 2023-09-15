## Lab Exercise 9/21/2023 Problem 1
## Author: nmessa
## creates a reversed string
def reverseString(s):
    newString = ""
    for i in range(len(s)-1, -1, -1):
        newString += s[i]
    return newString

#Test Code
print(reverseString("Hello World!!!"))

##Output
##!!!dlroW olleH



    
