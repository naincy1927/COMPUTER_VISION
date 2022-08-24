import cv2 
img1 = cv2.imread("C:\\Users\\naincy\\Desktop\\DATA_SET_\\BEACH.jpg",-1) ## we use -1 to increas the pixel value of the image in coloured form
img1 = cv2.resize(img1,(1200,1200))
cv2.imshow("orignal",img1)
k = cv2.waitKey() 
if k == ord("s"):
    cv2.imwrite("D:\\output.png",img1)
else:
    cv2.destroyAllWindows
### Here after seeing the output image if user wants to save the iamge they have to press "s" else the programm will clear the output

