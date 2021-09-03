import numpy as np
import cv2
def main():
    #carlos Jesus Olea Diaz
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = np.zeros((512, 480, 3),dtype=np.uint8)
    img.fill(255)
    #Rojo
    cv2.ellipse(img, (235, 130), (50, 50), 125, 0, 286, (0, 0, 255), 30)
    #Azul
    cv2.ellipse(img, (310, 256), (50, 50), 305, 0, 284, (255,0,0), 30)
    #Verde
    cv2.ellipse(img, (160, 256), (50, 50), 10, 0, 288, (0, 255, 0), 30)
    cv2.putText(img, "OpenCV", (120, 420), font, 2, (0, 0 ,0), 2, cv2.LINE_AA)
    pts = np.array([ [400, 350],[251, 350], [235, 255], [170, 255], [235, 140], [310, 250], [370,140 ]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (255, 255, 255), 11)
    cv2.imshow("OpenCV", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()