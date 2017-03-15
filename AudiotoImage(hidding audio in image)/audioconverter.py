import ffmpy

def mp3towav(src,dest):
    ff = ffmpy.FFmpeg(
        inputs={src: None},
        outputs={dest: None})
    ff.run()


def wavtomp3(src,dest):
    ff = ffmpy.FFmpeg(
        inputs={src: None},
        outputs={dest: None})
    ff.run()


def openmp3(filename):
    with open(filename,'rb') as f:

       while f.readable():
            print (f.read(1))