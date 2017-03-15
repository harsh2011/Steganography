import cv2
import numpy as np
import soundfile as sf
import audioconverter


def imagetoaudio(filename,outputdes):

    img = cv2.imread(filename,cv2.IMREAD_UNCHANGED)


    allchannel  =  np.array(img)

    allchannel = np.transpose(allchannel)



    d2channel1front  = np.array(allchannel[0])

    d2channel2front  = np.array(allchannel[1])

    d2channel1end  = np.array(allchannel[2])

    d2channel2end  = np.array(allchannel[3])

    channel1front  = np.reshape(d2channel1front,(1,-1))
    channel1front  = np.array(channel1front[0])
    channel1end  = np.reshape(d2channel1end,(1,-1))
    channel1end  = np.array(channel1end[0])
    channel2front  = np.reshape(d2channel2front,(1,-1))
    channel2front  = np.array(channel2front[0])
    channel2end  = np.reshape(d2channel2end,(1,-1))
    channel2end  = np.array(channel2end[0])

    channel1 = (channel1front*256 + channel1end)
    channel2 = (channel2front*256 + channel2end)

    channel1 = channel1.astype(int)
    channel2 = channel2.astype(int)

    channel1 = channel1-32768
    channel2 = channel2-32768

    data = [channel1,channel2]

    data = np.array(data)
    data = np.transpose(data)

    data = data[0:14467107]


    npdata = data.astype('int16')

    sf.write(outputdes,npdata, 44100)


