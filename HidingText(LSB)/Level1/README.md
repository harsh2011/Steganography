This is the first code I have wrote to HIDE data in IMAGE.

This is the LEVEL1

-> It hide the data in LSD bits
-> Image pixel must have 4 value(R,G,B,A)
-> File of image must be PNG (Because PNG is the losseless compression)(while, on other side JPEG doesn't work because it change the image by 10% but human eye can't deteted it)
-> Using 8 bits ascii value of character

STEPS 1:
Read PNG image to hide data inside that image (img)
convert a text in 8 bits ascii
    'HIDE' -> [71,72,68,69]
    

STEP 2:
convert disintegrate each ascii in 4 value
    71 bin-> 0100 0111 
    0100 0111 -> 01 , 00 , 01 , 11 -> 1 , 0 , 1 , 3
    71 -> [1,0,1,3]
    'HIDE' -> [[1,0,1,3],[1,0,2,0],[1,0,1,0],[1,0,1,1]]
    
STEP 3:
convert 1d array in 2d 
    [[1,0,1,3],[1,0,2,0],[1,0,1,0],[1,0,1,1]] -> [[[1,0,1,3],[1,0,2,0]],
                                                  [[1,0,1,0],[1,0,1,1]]]
                                                  
STEP 4:
