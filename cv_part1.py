import cv2
img = cv2.imread("C:\\Users\\naincy\\Desktop\\DATA_SET_\\BIRD AND RED FLOWER.jpg",1) ##adding 1 as an integer value here because it's an 3 scale picture (coloured image)
img = cv2.resize(img,(800,1200))
cv2.imshow("meri chidiya phool ko dekhti hui kitni pyari lag rhi h (-_-)",img)


img2 = cv2.imread("C:\\Users\\naincy\\Desktop\\DATA_SET_\\BIRD AND RED FLOWER.jpg",0) ##adding 0 as an integer value here becaus now we want an greay scale picture (blak and whight image)
img2 = cv2.resize(img2,(800,1200))
cv2.imshow("meri chidiya phool ko dekhti hui kitni pyari lag rhi h",img2)


cv2.waitKey()
cv2.destroyAllWindows()
