import cv2
import numpy as np

def addALine(img):
    for i in range(0, 200):
        px = img[i, 100]
        print px
        img[i, 100] = [255, 255, 255]

def copyARegion(img):
    region = img[300:350 , 480:550]
    img[0:50 , 0:70] = region

def splitAndMerge(img):
    b,g,r = cv2.split(img)
    print r
    r_row = []
    for i in range (0,640):
        r_colume = []
        for j in range(0,1024):
            r_colume.append(0)
        r_row.append(r_colume)
    print r_row
    # img = cv2.merge((b,g,r_row))


def processImage(img):
    splitAndMerge(img)


img = cv2.imread('img/view_backup.jpg',1)
processImage(img)

cv2.imshow('image', img)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('new_view.png',img)
    cv2.destroyAllWindows()

