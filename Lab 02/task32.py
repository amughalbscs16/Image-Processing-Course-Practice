from PIL import Image,ImageFilter
img = Image.open('task32.jpg')
smoothenedimage = img.filter(ImageFilter.SMOOTH_MORE)
smoothenedimage.save("task32smoothened.jpg")