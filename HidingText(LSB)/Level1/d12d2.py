

def d1arraytod2array(array):

    length = len(array)
    sr = length**(0.5)


    print(sr)

    print(int(sr))

    if(sr>int(sr)):
        sr  = int(sr)+1

    print(sr)

    numberofzeropadding = (sr*sr) - length
    paddedarray = paddingzeroesattheend(array, numberofzeropadding)
    new2darray = converter1dto2d(paddedarray, sr)

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