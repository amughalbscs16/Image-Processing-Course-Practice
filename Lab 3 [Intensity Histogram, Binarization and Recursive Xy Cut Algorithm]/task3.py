from PIL import Image,ImageDraw
import matplotlib.pyplot as plt
img1 = Image.open("images\\XY-cutss.png").convert("L")
width,height = img1.size
intensities = [0 for y in range(0,height)]
for x in range(0,width):
	for y in range(0,height):
		if (img1.getpixel((x,y)) < 128):
			intensities[y]+=1;
threshold = 30;
draw = ImageDraw.Draw(img1)
for y in range(0,height):
	if intensities[y] < 20:
		draw.line((0,y) + (width-1,y) , fill=0)
img1.show()





