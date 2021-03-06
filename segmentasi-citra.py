import cv2
import numpy as np
import matplotlib.pyplot as plt
 
#baca gambar
butterfly=cv2.imread('kupu-kupu.jpg')
#convert BGR ke RGB
butterfly=cv2.cvtColor(butterfly,cv2.COLOR_BGR2RGB)
#convert RGK ke HSV
hsv_butterfly=cv2.cvtColor(butterfly, cv2.COLOR_RGB2HSV)
 
#deklarasi batas bawah (orange cerah)
light_orange=(1,190,200)
#deklarasi batas atas (dark orange)
dark_orange =(18, 255, 255)
 
#tresholding
mask=cv2.inRange(hsv_butterfly,light_orange,dark_orange)
#impose gambar asli dengan mask
result=cv2.bitwise_and(butterfly,butterfly, mask=mask)
 
#plotiing
plt.subplot(2,2,1)
plt.imshow(butterfly)
plt.subplot(2,2,2)
plt.imshow(hsv_butterfly)
plt.subplot(2,2,3)
plt.imshow(mask)
plt.subplot(2,2,4)
plt.imshow(result)
plt.show()
