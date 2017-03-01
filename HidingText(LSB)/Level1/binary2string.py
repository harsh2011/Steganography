
def imagetobinarytochartostring(image):
    str = ''
    for pixel in image:
        i = 0
        char =0;
        for bits in pixel:
            char = char | bits<<(i*(2))
            i=i+1
        if(char==3):
            break
        str = str + chr(char)

    return str

# str = imagetobinarytochartostring([[0, 2, 2, 1],[0, 2, 2, 1]])
# print(str)