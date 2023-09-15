## Lab Exercise 9/20/2023 Problem 3
## Author: nmessa
## Solves locker puzzle
##
## Shut = X
## Open = O
## X = False
## O = True

#Create an empty list
lockers = []

#initialize lockers to all shut (False)
for _ in range(1001):
    lockers.append(False)

#students traverse lockers
for student in range(1, 1001):
    for locker in range(1, 1001):
        if locker % student == 0:
            lockers[locker] = not lockers[locker]

#print locker state
for locker in range(1,1001):
    if lockers[locker]:
        print ('O', end = '')
    else:
        print ('X', end = '')



        



    
