import numpy as np 
import cv2 as c
img = np.ones([1200,1200,3],np.uint8)*250
c.imshow("white img",img)
c.waitKey()
c.destroyAllWindows()