## Lab Exercise 9/21/2023 Problem 3
## Author: nmessa
## Calculate a gymnastic score
def gymScore(scores):
    minimum = min(scores)
    maximum = max(scores)
    total = sum(scores) - maximum - minimum
    average = total/3
    return average

#Test Code
testScores = [1,7,8,9,10]
print(gymScore(testScores))   #8.0

        



    
