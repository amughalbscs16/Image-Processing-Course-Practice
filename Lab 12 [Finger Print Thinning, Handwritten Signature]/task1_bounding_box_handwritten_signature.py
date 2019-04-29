from PIL import Image, ImageDraw
import cv2 as cv
im = Image.open("signature.png").convert("L")
im.show()
width, height = im.size
left = width;
right= 0;
top = height;
bottom = 0;
#print(height,width)
for x in range(0,width):
    for y in range(0,height):
        color = im.getpixel((x,y))
        #print(color)
        if color < 127:
            if x > right:
                right = x;
            if x < left:
                left = x;
            if y > bottom:
                bottom = y;
            if y < top:
                top = y;
im.close()
img = cv.imread('signature.png',0) #in Grey Scale
crop_img = img[top:bottom, left:right]
cv.imshow("cropped", crop_img)
cv.imwrite('finalsignature.png',crop_img)
cv.waitKey(0)
print(top,bottom,right,left)


