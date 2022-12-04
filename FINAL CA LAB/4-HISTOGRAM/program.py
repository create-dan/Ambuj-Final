import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

dog = cv2.imread("dog.jpeg")
dog = cv2.resize(dog, (800, 600))
cv2.imshow('Original', dog)

dogGray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
dogGray = cv2.convertScaleAbs(dogGray, alpha=1.10, beta=-20)
s = dogGray.shape

def Hist(image):
    s = image.shape
    H = np.zeros(shape=(256,1))
    for i in range(s[0]):
    	for j in range(s[1]):
    	    k = image[i, j]
    	    H[k,0] = H[k,0]+1
    return H
    
H = Hist(dogGray)
plt.plot(H)
# plt.show()

# From here equalization of histogram starts.
x = H.reshape(1, 256)

y = np.array([])
y = np.append(y, x[0,0])

for i in range(255):
    k = x[0, i+1] + y[i]
    y = np.append(y, k)
   
y = np.round((y/(s[0]*s[1])) * 255)

for i in range(s[0]):
    for j in range(s[1]):
    	k = dogGray[i,j]
    	dogGray[i,j] = y[k]
    	
cv2.imshow('Normalized', dogGray)

equalizehist = Hist(dogGray)
plt.plot(equalizehist)
plt.show()

cv2.waitKey(0)
