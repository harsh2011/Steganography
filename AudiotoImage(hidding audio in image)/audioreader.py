import soundfile as sf
import numpy as np
import cv2


def audiotoimage(filename):

    data, samplerate = sf.read(filename,dtype='int16')
    print(len(data))

    print(data[120000])

    print(samplerate)

    npdata =  np.array(data)
    npdatat  = npdata.transpose()

    channel1 = npdatat[0]
    channel2 = npdatat[1]

    def paddingzeroesattheend(array,no):
        arr=[]
        i = 0
        while(i<=no):
            arr.append(0)
            i=i+1

        array = np.append(array,arr)
        return array



    length =  len(channel1)
    square = length**(0.5)

    if (square> int(square)):
        square = int(square) + 1

    print(square)



    channel1 = paddingzeroesattheend(channel1,((square*square)-len(channel1)-1))
    channel2 = paddingzeroesattheend(channel2,((square*square)-len(channel2)-1))

    channel1 = np.array(channel1)
    channel2 = np.array(channel2)

    channel1 = channel1 + 32768
    channel2 = channel2 + 32768

    channel1front = channel1 / 256
    channel1end = channel1front - channel1front.astype(int)
    channel1end = channel1end*256

    channel1front = channel1front.astype(int)
    channel1end = channel1end.astype(int)

    channel2front = channel2 / 256
    channel2end = channel2front - channel2front.astype(int)
    channel2end = channel2end*256

    channel2front = channel2front.astype(int)
    channel2end = channel2end.astype(int)




    d2channel1front  = np.reshape(channel1front,(square,square))
    d2channel1end  = np.reshape(channel1end,(square,square))
    d2channel2front  = np.reshape(channel2front,(square,square))
    d2channel2end  = np.reshape(channel2end,(square,square))

    allchannel = [d2channel1front,d2channel2front,d2channel1end,d2channel2end]

    allchannel = np.array(allchannel)


    allchannel = np.transpose(allchannel)
    print(allchannel)

    cv2.imwrite("image.png", allchannel,[cv2.IMWRITE_PNG_COMPRESSION,9])

    print("done2")













# channel1int = []
# channel1float = []
#
# for data in channel1:
#     fv = (data - int(data)) * 255
#     fv = int(fv)
#     channel1float.append(fv)
#     channel1int.append(int(data))
#
# channel2int = []
# channel2float = []
#
# for data in channel2:
#     fv = (data - int(data)) * 255
#     fv = int(fv)
#     channel2float.append(fv)
#     channel2int.append(int(data))
#
#
# channel1int  = np.array(channel1int)
# channel1float  = np.array(channel1float)
# channel2int  = np.array(channel2int)
# channel2float  = np.array(channel2float)
#
#
#
# print("done1")
