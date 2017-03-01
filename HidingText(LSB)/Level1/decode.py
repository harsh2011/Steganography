def timetodecode(image , key):

    hidearray = []
    y  =key[0]
    x  =key[1]
    height_encode_img  = key[2]
    width_encode_img  = key[3]

    # print(height_encode_img)
    # print(width_encode_img)

    height = y
    i = 0
    while (i < height_encode_img):
        width = x
        j = 0
        while (j < width_encode_img):
            pixel  = image[height][width]
            hiddenpixel = []
            indexs = [0, 1, 2, 3]
            for index in indexs:
                hiddenpixel.append(pixel[index]& 0b00000011)

            hidearray.append(hiddenpixel)
            j = j + 1
            width = width + 1

        i = i + 1
        height = height + 1

    # print('decoded')
    print(hidearray)
    return hidearray
    # print('yes')

