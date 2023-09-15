##Lab Exercise 9/18/2023 Problem 6
##Author: nmessa
##counts the words in a string

#This function returns the number of "words" contained in
#the string passed as a parameter
def countWords(string):
    #method 1
##    count = string.count(' ')
##    return count + 1

    #method 2
##    words = string.split(' ')
##    return len(words)

    #method 3
    count = 0
    for ch in string:
        if ch == ' ':
            count += 1
    return count + 1
            
    
#Test code
print (countWords('Chicago Transit Authority')) #3
print (countWords('I really love pizza flavored cheesecake')) #6



