import sys, random, argparse
import numpy as np
import math
from PIL import Image

#Grayscale image mapping
gscale1 = "$@B%8&WM#*oahkbdpqwmZ0oQLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!1I;:,\"^''. "
gscale2 = '@%#*+=-:. '

#Calculate the average luminescence
def getAverageL(image):
    im = np.array(image)
    w, h = im.shape
    return np.average(im.reshape(w*h))

#convert pixels in JPG image to grayscale and to ASCII characters
def convertImageToAscii(filename, cols, scale, moreLevels):
    global gscale1, gscale2

    #Open the image and convert to luminescence values
    image = Image.open(filename).convert('L')

    #Get the size of the image
    W, H = image.size[0], image.size[1]
    print("Input image dimensions: %d x %d" %(W, H))

    #calculate the rows and columns of the pixel array
    w = W/cols
    h = w/scale
    rows = int(H/h)

    #Print out stats for image (useful in optimizing)
    print("cols: %d, rows: %d" % (cols, rows))
    print("Tile dimensions: %d x %d" %(w,h))

    if cols > W or rows > H:
        print ('Image too small for specified cols')
        exit(0)

    aimg = []   #create a list to hold the ASCII image characters
    #process array by row
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)

        if j == rows -1:
            y2 = H

        aimg.append("")

        for i in range(cols):
            x1 = int(i*w)
            x2 = int((i+1)*w)
            if i == cols - 1:
                x2 = W
            img = image.crop((x1,y1,x2,y2))
            avg = int(getAverageL(img))

            #determine which grayscale map to use
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)] #70 levels of grayscale
            else:
                gsval = gscale2[int((avg*9)/255)]   #10 levels of grayscale
            aimg[j] += gsval

    return aimg

def main():
    outFile = 'out.txt'

    print ('Generating ASCII Art .....')
    #call the conversion function
    #convertImageToAscii(fileName, cols, scale, moreLevels)
    aimg = convertImageToAscii('alfred.jpg', 239, 1.0, True)

    #Write ASCII Image characters to file
    f = open(outFile, 'w')
    for row in aimg:
        f.write(row + '\n')
    f.close()

main()
        



