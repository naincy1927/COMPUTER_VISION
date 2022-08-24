
import cv2
path = input(" enter the path of the picture :- ")
img1 = cv2.imread(path,0)
# img1 = resize(img1,(560,700))
cv2.imshow(" converted image",img1)
cv2.waitKey()
cv2.destroyAllWindows()
# "C:\Users\naincy\Desktop\DATA_SET_\DOGS.jpg"