from PIL import Image
import matplotlib.pyplot as plt
image = Image.open("dollor.jpg").convert("L")
width,height = image.size
L = 256;
pixels = image.load()
planevalue = 1;
for j in range(0,8):
        for x in range(0,width):
            for y in range(0,height):
                if pixels[x,y] & planevalue == 0:
                    pixels[x,y] = 0;
                else:
                    pixels[x,y] = 255;
        image.save("dollarplane"+str(j)+".jpg")
        image.show()
        image = Image.open("dollor.jpg").convert("L")
        pixels = image.load()
        planevalue*=2;
