import qrcode
import cv2
img = qrcode.make('hello world')
img.save('test.png')
img = cv2.imread('test.png')
cv2.imshow(img)
