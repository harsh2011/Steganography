
import cv2

from string2binary import stringtochartobinarytoimage
from d12d2 import d1arraytod2array
from encode import timetoencode
from decode import timetodecode
from binary2string import imagetobinarytochartostring

img = cv2.imread("Image\\Untitled.png")
img = cv2.cvtColor(img,cv2.COLOR_RGB2RGBA)

width = len(img)
heigth = len(img)

min = 0

if(width<heigth):
    min = width-3
    min = int(min * min)
else:
    min = heigth-3
    min = int(min * min)

print("minimum character "+str(min))

str = str(input("Enter string to hide: "))

d1 =  stringtochartobinarytoimage(str+chr(3))
print(d1)
d2 = d1arraytod2array(d1)
print(d2)
key = timetoencode(img,d2,"encode")
print(key)
encodedimg = cv2.imread("encode.png",cv2.IMREAD_UNCHANGED)
decode = timetodecode(encodedimg,key)
print(decode)
str = imagetobinarytochartostring(decode)
print(str)


