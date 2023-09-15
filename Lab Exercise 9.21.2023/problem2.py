## Lab Exercise 9/21/2023 Problem 2
## Author: nmessa
## Calculate a series of recipricols
def calcSeries(terms):
    total = 0
    for n in range(1, terms+1):
        total += 1/n
    return total

#Test Code
print(calcSeries(10))   #2.9289682539682538

        



    
