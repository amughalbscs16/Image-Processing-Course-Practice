from PIL import Image
img = Image.open('task31.jpg').convert('LA')
img.save('task31greyscale.png')