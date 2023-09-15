##Lab Exercise 9/18/2023 Problem 5
##Author: nmessa
##counts the vowels in a string

#This function will return the number of vowels contained in the
#string passed as a parameter
def countVowels(string):
    count = 0
    vowels = "aeiou"
    string = string.lower()
    for letter in string:
        if letter in vowels:
            count += 1
    return count
    
#Test code
print (countVowels('Chicago Transit Authority')) #9
print (countVowels('I really love pizza flavored cheesecake')) #15



