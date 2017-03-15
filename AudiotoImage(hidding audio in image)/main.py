import audioconverter
import audioreader
import audiowriter


audioconverter.mp3towav('EncodeAudio/matargasti.mp3','EncodeAudio/output.wav')

audioreader.audiotoimage('EncodeAudio/output.wav')

audiowriter.imagetoaudio('image.png','DecodeAudio/final.wav')

audioconverter.wavtomp3('DecodeAudio/final.wav','DecodeAudio/final.mp3')


