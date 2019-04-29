from PIL import Image,ImageDraw
import cv2 as cv
im = Image.open("finalsignature.png").convert("L")
width,height = im.size
print(width,height)
cx = 0;
cy = 0;
n = 0;
for x in range(0,width):
    for y in range(0,height):
        if (im.getpixel((x,y)) < 127):
            cx = cx + x;
            cy = cy + y;
            n = n + 1
cx = int(cx / n)
cy = int(cy / n)
draw = ImageDraw.Draw(im)
draw.rectangle([cx-2,cy-2,cx+2,cy+2], fill="RED")
im.show()
im.save("signaturecentroid-"+str(cx)+"-"+str(cy)+".png");

print(cx,cy)
