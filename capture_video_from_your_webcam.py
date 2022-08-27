import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print(cap)
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True :
        frame = cv2.resize(frame,(700,450))
    
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(1) == ord("q"):
            break 
cap.release()
cv2.destroyAllWindows()