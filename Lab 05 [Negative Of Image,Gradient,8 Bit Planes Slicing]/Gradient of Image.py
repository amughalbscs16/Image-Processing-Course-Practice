from PIL import Image
import matplotlib.pyplot as plt
img1 = Image.open("lenacolor.jpg").convert("L")
width,height = img1.size
L = 256;
pixels = img1.load()
for x in range(0,width-1):
    for y in range(0,height):
        pixels[x,y] = abs(pixels[x+1,y] - pixels[x,y])
img1.show()
img1.save("lenagradient.jpg")
