import cv2

img=cv2.imread("galaxy.jpg",0)      #1 for color, 0 for grayscale, -1 for color image and transparency


print(type(img))        #type
print(img)              #numpy array, ... means python cant display all numbers in terminal
print(img.shape)        #numbers across by numbers down
print(img.ndim)         #number of dimensions

#resized_image=cv2.resize(img,(1000,500)) #resized so it can fit in window on screen
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))   #first tuple is width, second tuple is height

cv2.imshow("Galaxy",resized_image)
#cv2.imwrite("Galaxy_resized.jpg",resized_image)
cv2.waitKey(0)   #in milliseconds, 0 means user can press exit button to exit
cv2.destroyAllWindows()
