

def d1arraytod2array(array):

    length = len(array)
    sr = length**(0.5)
    if(sr==1):
        return array
    elif(sr>1 and sr<=2):
        numberofzeropadding = 4-length
        paddedarray = paddingzeroesattheend(array,numberofzeropadding)
        new2darray = converter1dto2d(paddedarray, 2)
    elif (sr > 2 and sr <= 3):
        numberofzeropadding = 9 - length
        paddedarray = paddingzeroesattheend(array, numberofzeropadding)
        new2darray = converter1dto2d(paddedarray,3)
    elif (sr > 3 and sr <= 4):
        numberofzeropadding = 16 - length
        paddedarray = paddingzeroesattheend(array, numberofzeropadding)
        new2darray = converter1dto2d(paddedarray, 4)
    elif (sr > 4 and sr <= 5):
        numberofzeropadding = 25 - length
        paddedarray = paddingzeroesattheend(array, numberofzeropadding)
        new2darray = converter1dto2d(paddedarray, 5)
    elif (sr > 5 and sr <= 6):
        numberofzeropadding = 36 - length
        paddedarray = paddingzeroesattheend(array, numberofzeropadding)
        new2darray = converter1dto2d(paddedarray, 6)
    elif (sr > 6 and sr <= 7):
        numberofzeropadding = 49 - length
        paddedarray = paddingzeroesattheend(array, numberofzeropadding)
        new2darray = converter1dto2d(paddedarray, 7)
    elif (sr > 7 and sr <= 8):
        numberofzeropadding = 64 - length
        paddedarray = paddingzeroesattheend(array, numberofzeropadding)
        new2darray = converter1dto2d(paddedarray, 8)

    return new2darray

def paddingzeroesattheend(array,no):
    i = 0
    while(i<=no):
        array.append([0,0,0,0])
        i=i+1

    return array

def converter1dto2d(array,no):
    new2darray = []
    i =0
    start = 0
    end = no-1
    while(i<no):
        temp = []
        j = start
        while(j<=end):
            temp.append(array[j])
            j=j+1
        new2darray.append(temp)
        start = start+no
        end = end+no
        i=i+1

    return new2darray