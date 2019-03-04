from PIL import Image
import matplotlib.pyplot as plt
img1 = Image.open("lenacolor.jpg")
width,height = img1.size
L = 256;
pixels = img1.load()
print(pixels[0,0])
for x in range(0,width):
    for y in range(0,height):
        pixelxy = list(pixels[x,y])
        #Used range and len to use the reference
        for i in range(0,len(pixelxy)):
                pixelxy[i] = abs(L-1-pixelxy[i])
        pixels[x,y] = tuple(pixelxy)
img1.show()
img1.save("lenacolornegative.jpg");
