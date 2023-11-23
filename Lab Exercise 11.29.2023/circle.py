##Circle class definition
##Author: 
##Date: 1/29/2023

from geometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, p1,r):
        GeometricObject.__init__(self)
        self.center = p1
        self.radius = r
        
    def _draw(self,aturtle):
        #Add code here
        
