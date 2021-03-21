from PIL import Image
import sys
import os.path
from os import path

if(len(sys.argv) != 2):
    print("Provide png file name as argument...")
    exit()

filename = sys.argv[1]

if(not os.path.exists(filename)):
    print("The provided file cannot be found...")
    exit()

try:
    im = Image.open(filename, 'r')
except IOError:
    print("Error opening " + filename)

pix_val = list(im.getdata())

count = {}

highestVal = 0
highestRGBA = ""

for val in pix_val:
    if(val[3] == 0):
        continue
    # use flat value as key
    strValue = str(val[0]) + str(val[1]) + str(val[2]) + str(val[3])
    try:
        count[strValue] += 1
        if count[strValue] > highestVal:
            highestRGBA = val
            highestVal = count[strValue]
    except KeyError:
        count[strValue] = 0
    

print("Pixel count mode is")
print("R:" +  str(highestRGBA[0]))
print("G:" +  str(highestRGBA[1]))
print("B:" +  str(highestRGBA[2]))
print("A:" +  str(highestRGBA[3]/255))
print("Seen " + str(highestVal) + " times")