import cv2 
## we import opencv as cv2 because the devlopers named the pakage/module as cv2 

img1 = cv2.imread("C:\\Users\\naincy\\Desktop\\DATA_SET_\\BEACH.jpg",1) 
#always remmember to add // while writting an path else it will relese an error

img1 = cv2.resize(img1,(1200,1200))
 ## resize your image if needed

cv2.imshow("orignal",img1)
 # here " orignal " is our window name where we'll see our image 

cv2.waitKey() 
# it holds the output window. we can add any integer number here . if we want aur output to be visable for 3 sec only than we can add 3 as it's parametere 

cv2.destroyAllWindows()
 # cleres the priviously done operations
