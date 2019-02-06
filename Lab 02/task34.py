import sys
import numpy as np
import matplotlib.pyplot
import matplotlib.image

file = "task34.jpg"
img = matplotlib.image.imread(file)
gray_img = np.dot(img[...,:3], [0.299, 0.587, 0.114])
matplotlib.pyplot.imshow(gray_img, cmap = matplotlib.pyplot.get_cmap('gray'))
matplotlib.pyplot.show()
outFileName = file.split('.')[0] + "_grayscale(manual).jpg"
matplotlib.pyplot.imsave(outFileName, gray_img, cmap="gray")
print("Grayscale")
print("Image", file, "Converted to", outFileName)