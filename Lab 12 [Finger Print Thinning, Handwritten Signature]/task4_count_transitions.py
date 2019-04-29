import cv2 as cv
from PIL import Image
count = [0,0,0,0]
img = Image.open("signaturecentroid-109-47.png").convert("L")
width,height = img.size
cx = 50
cy = 36
prev = img.getpixel((0,0))
for x in range(0,width):
    for y in range(1,height):
        curr = img.getpixel((x,y))
        if curr > 127 and prev < 127:
            if (x <= cx and y <= cy):
                count[0] +=1 ;
            elif (x > cx and y <= cy):
                count[1] += 1;
            elif (x <= cx and y > cy):
                count[2] += 1;
            elif (x > cx and y > cy): 
                count[3] += 1;
        prev = curr;

print(count)
