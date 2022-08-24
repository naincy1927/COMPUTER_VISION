import cv2
cap = cv2.VideoCapture("C:\\Users\\naincy\\Desktop\\DATA_SET_\\FLOWER_VIDEO.mp4")
# cap = cv2.resize(cap,(1200,2000))
while True:
    ret , frame = cap.read()
    cv2.imshow("frame",frame)
    cv2.waitKey(25)
    cap.release()
    cv2.destroyAllWindows