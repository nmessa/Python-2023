## Lab Exercise 11/9/2023 Problem 1 and 2
## Author: nmessa
## Program to calculate the distance between two points
## Points may be in a plane or a 3D space

import math
from point import Point
from point3D import Point3D

def distance(p1, p2):
    #Add code here

def distance3D(p1, p2):
    #Add code here

#Test code for 2D distance
#define two points
p1 = Point(2,2)
p2 = Point(1,1)

print (distance(p1, p2))   # 1.4142135623730951

#Test code for 3D distance
#define two points
p1 = Point3D(1,1,1)
p2 = Point3D(0,0,0)

print (distance3D(p1, p2))   # 1.7320508075688772


