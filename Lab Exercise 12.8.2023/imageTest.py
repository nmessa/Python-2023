##Lab Exercise 12/8/2023
##Author: 

from images import Image

def main(filename = "smokey.gif"):
    image = Image(filename)
    image.draw()
    blackAndWhite(image)
    image.draw()
    grayScale(image)
    image.draw()
    image = detectEdges(image,40)
    image.draw()

def blackAndWhite(image):
    #Add code here
    

def grayScale(image):
    #Add code here
    

def detectEdges(image, amount):
    

main()
