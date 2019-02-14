from PIL import Image

img1 = Image.open("images\\B1.png").convert("L")
img2 = Image.open("images\\B2.jpg").convert("L")
img3 = Image.open("images\\B3.jpg").convert("L")
images = [img1,img2,img3];
for imgg in images:
	width,height = imgg.size
	pixels = imgg.load()
	for x in range(0,width):
		for y in range(0,height):
			if pixels[x,y] < 128:
				pixels[x,y] = 0;
			else:
				pixels[x,y] = 255;
	imgg.show()

