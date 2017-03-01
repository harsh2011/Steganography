

def stringtochartobinarytoimage(str):

    binaryimg = []
    for letter in str:
        #print ("."+letter+".")
        #print (ord(letter))
        a = ord(letter)
        #print(bin(a))
        pixel = []
        i =0
        while(i<4):
            last2 = a & 3
            pixel.append(last2)
            binlast2 = bin(last2)
            #print (binlast2)
            a = a>>2
            i=i+1
        binaryimg.append(pixel)

    return binaryimg



