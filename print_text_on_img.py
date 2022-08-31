from multiprocessing.connection import wait
from tkinter import font
import cv2 as c
from cv2 import imshow
import numpy as np
img = c.imread("C:\\Users\\naincy\\Desktop\\DATA_SET_\\BIRD AND RED FLOWER.jpg",-1)
img = c.resize(img,(500,500))
img = c.line(img,(0,0),(200,200),(154,92,424),8)
img = c.arrowedLine(img,(0,0),(200,200),(154,92,424),8)
img = c.rectangle(img,(0,0),(200,200),(154,92,424),8)
img = c.rectangle(img,(0,0),(200,200),(154,92,424),-8)
img = c.circle(img,(100,200),90,(154,92,424),-1)
font = c.FONT_ITALIC
img = c.putText(img,"red_flower",(50,450),font,1,(0,125,255),4,c.LINE_AA)
c.imshow("meri photu",img)
k = c.waitKey()
if k==ord("s"):
    c.imwrite("D:\\meri_photu.png",img)
else:
    if k == ord("q"):
        c.destroyAllWindows()