This is the first code I have wrote to HIDE data in IMAGE.

This is the LEVEL1

1.It hide the data in LSD bits

2.Image pixel must have 4 value(R,G,B,A)

3.File of image must be PNG (Because PNG is the losseless compression)(while, on other side JPEG doesn't work because it change the image by 10% but human eye can't deteted it)

4.Using 8 bits ascii value of character

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

select position to hide the 2d array store it in key

    key = [y position,x postion,heigth,width]
    
STEP 5:

Hidding part

Converting 2 LSB bits to ZERO

Then OR those bits with hidding data bits to hide bits 

    Hidding data => [1,0,1,3] 
    Pixel to hide => [12,54,14,255] (RGBA)
    
    now,
    (12 & (~3)) | 1 = 13
    (54 & (~3)) | 1 = 52
    (14 & (~3)) | 1 = 13 
    (255 & (~3)) | 3 = 255
    
    //before hiding
    [12,54,14,255]
    //after hiding
    [13,52,13,255]
