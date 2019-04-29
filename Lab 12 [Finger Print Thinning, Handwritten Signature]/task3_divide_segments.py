from PIL import Image, ImageDraw
import cv2 as cv

cx = 109;
cy = 47;

img = cv.imread("signaturecentroid-109-47.png",0)
height,width = img.shape
cv.rectangle(img,(0,0),(cx,cy),(0,0,0),1)
cv.rectangle(img,(cx,0), (width,cy),(0,0,0),1)
cv.rectangle(img, (0,cy), (cx,height-1),(0,0,0),1)
cv.rectangle(img, (cx,cy), (width,height-1), (0,0,0),1)
cv.imshow("Image", img)
cv.imwrite("four-segments-image.png",img);
