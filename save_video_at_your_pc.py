import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)  

## if you are working on over 3.8 version of python than you should use this secound parameter . so that you won't get any warning

fourcc = cv2.VideoWriter_fourcc(*"XVID")

## here 'fourcc' is a function that inform the computer about which formate the video should be saved 
## ther is multiple formate available for example :- DIVX , XVID , MJPG , X264 , WMV1 , WMV2 .
## but " XVID" is conciderd as the best way to write / capture your video.

output = cv2.VideoWriter("D:\\output.avi",fourcc,20.0,(640,480),0)
print(cap)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True :
        frame = cv2.resize(frame,(700,450))
    
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(1) == ord("q"):
            break 
cap.release()
output.release()
cv2.destroyAllWindows()