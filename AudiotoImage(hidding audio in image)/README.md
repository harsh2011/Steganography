Hiding AUDIO in the form of IMAGE

Libraries used:-

1. ffmpy (python)
  For file conversion
2. soundfile (python)
  Read and Write the WAV file in python
3. numpy (pyhton)
  Handling N dimensional array
4. cv2 (python)
  Use for writing the PNG image
  
Reading of WAV file

read() method of soundfile returns two thing 
1.samplerate
2.data (frames)(data types are (float,int))(array of data)

As this Program reads int16 ,datatype. range of (-32768 to 32767)

One of the given data

	data = 6000 //range of (-32768 to 32767)
	data = data + 32768
	// divide data bits(data is of 16 bits)
	datafront = first8bitsof(data) // 8bits
	datalast = last8bitsof(data) // 8bits
	
then,for the 2 channel in the data of 16 bits convert in 4 channel of 8 bits.which easy represent the image pixel value between 0 to 255

Using open write the data in image form. But image file must be PNG(lossless compression).

Here is an ENCODE IMAGE:-

![Screenshot](image.png)

	

  






