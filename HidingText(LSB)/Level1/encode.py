import  cv2
import random

def timetoencode(image,message,filename):
    key = []
    hidingarray = message

    # print(len(hidingarray))
    # print(len(image))
    # print(len(hidingarray[0]))
    # print(len(image[0]))

    if(len(image)>len(hidingarray) and len(image[0])>len(hidingarray[0])):

        y = random.randrange(3, len(image) - len(hidingarray))
        x = random.randrange(3,len(image[0])-len(hidingarray[0]))

        # print(y)
        # print(x)

        key.append(y)
        key.append(x)
        key.append(len(hidingarray))
        key.append(len(hidingarray[0]))

        height = y
        i = 0
        while(i<len(hidingarray)):
            width = x
            j = 0
            while(j<len(hidingarray[0])):
                pixel = image[height][width]
                hidingpixel  = hidingarray[i][j]
                indexs = [0,1,2,3]
                for index in indexs:
                    last2zero = pixel[index] & 0b11111100
                    pixel[index] = last2zero | hidingpixel[index]
                image[height][width] = pixel
                j = j+1
                width  = width +1

            i=i+1
            height = height+1

        # print('yes')

    cv2.imwrite(filename+".png", image)

    return key