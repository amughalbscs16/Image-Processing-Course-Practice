from PIL import Image
import matplotlib.pyplot as plt
img1 = Image.open("images\\B1.png").convert("L")
width,height = img1.size
intensities = [0 for y in range(0,256)]
print(intensities)
for x in range(0,width):
	for y in range(0,height):
		intensities[img1.getpixel((x,y))]+=1;
print(intensities)
plt.plot(intensities)
plt.show()