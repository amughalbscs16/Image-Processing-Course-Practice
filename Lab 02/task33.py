from PIL import Image,ImageFilter
img = Image.open('task33.jpg')
smoothenedimage = img.filter(ImageFilter.SHARPEN)
smoothenedimage.save("task33sharpen.jpg")