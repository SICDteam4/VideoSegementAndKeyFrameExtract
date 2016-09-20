#coding: utf-8
# import numpy as np
import cv2
import cPickle as pickle
# from matplotlib import pyplot as plt

def printt():
    print 'haha'
    return 'hello world!'

def get_frame_fps(vc , video_link):
    # 获取视频的帧数
    if vc.isOpened():
        video_fps = vc.get(cv2.cv.CV_CAP_PROP_FPS)
        return video_fps
    else:
        return 0

def get_frame_count(vc , video_link):
    if vc.isOpened():
        vc = cv2.VideoCapture(video_link)
        totalFrameNumber = vc.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
        return totalFrameNumber
    else:
        return 0

def get_image_histgram():
    # 获取图像直方图
    img = cv2.imread('img/image/1.jpg',0)
    hist = cv2.calcHist([img],[0],None,[256],[0,256])

    plt.subplot(221)
    plt.imshow(img, 'gray')

def frame_segmentation():
    video_link = 'video/xxx.flv'
    vc = cv2.VideoCapture(video_link)
    frametostart = 1
    frametostop = get_frame_count(vc , video_link)
    vc.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frametostart)

    c = frametostart
    unstop = 1

    while unstop:
        rval, frame = vc.read()
        cv2.imwrite('img/image/' + str(c) + '.jpg', frame)
        c = c + 1
        if c > frametostop:
            unstop = 0

    vc.release()
    cv2.destroyAllWindows()

def Bgr2Gray():
    for i in range(1 , 374):
        input_image = cv2.imread('img/image/'+ str(i) +'.jpg' , 0)
        cv2.imwrite('img/image/'+ str(i) +'_gray.jpg' , input_image)
    # cv2.cvtColor( input_image, cv2.COLOR_BGR2GRAY)

def readGrayValue():
    x = 50
    y = 100
    img = cv2.imread('img/image/1.jpg' , 1)
    value = img[x , y]
    img_Gray = cv2.imread('img/image/1.jpg', 0)
    grayValue = img_Gray[x, y]
    print value
    print grayValue

def calculateDF_colorDvalue_method(image_link_one , image_link_two):
    img1 = cv2.imread(image_link_one , 0)
    img2 = cv2.imread(image_link_two , 0)
    img_width = int(img1.shape[0])
    img_height = int(img1.shape[1])
    totalDF = 0
    for i in range(img_width):
        for j in range(img_height):
            df = img1[i,j] - img2[i,j]
            totalDF = totalDF + df
    totalDF = totalDF / (img_width * img_height)
    # print totalDF
    return totalDF

def calculateDF_histgramBased_method(image_link_one, image_link_two):
    img1 = cv2.imread(image_link_one , 1)
    img2 = cv2.imread(image_link_two , 1)
    img_width = int(img1.shape[0])
    img_height = int(img1.shape[1])
    totalDF = 0
    valid_count = 0
    for i in range(img_width):
        for j in range(img_height):
            df_R = min(img1[i,j][0] , img2[i,j][0])
            df_G = min(img1[i,j][1] , img2[i,j][1])
            df_B = min(img1[i,j][2] , img2[i,j][2])
            if img2[i,j][0] + img2[i,j][1] + img2[i,j][2] == 0:
                pass
            else:
                valid_count = valid_count + 1
                df_temp = df_R + df_G + df_B
                img2_temp = int(img2[i,j][0])  + int(img2[i,j][1]) + int(img2[i,j][2])
                df = float((df_R + df_G + df_B)) / float(int(img2[i,j][0])  + int(img2[i,j][1]) + int(img2[i,j][2]))
                df = round(df , 2)
                totalDF = totalDF + df

    totalDF = totalDF / (img_height * img_width)
    Z = 1 - totalDF
    return Z

def secenEdgeListProcess():

    f = open('C:\\Users\\oliverfan\\PycharmProjects\\opencv\\frameDiff.txt', 'r')
    dfList = pickle.load(f)
    f.close()

    edgeList = []
    for i in range( len(dfList) - 1 ):
        if abs(dfList[i]['df_value'] - dfList[i+1]['df_value']) > 0.10:
             edgeList.append(dfList[i])

    f = open('C:\\Users\\oliverfan\\PycharmProjects\\opencv\\shotBoundary.txt', 'w')
    pickle.dump(edgeList, f)
    f.close()


def secenEdgeDetection():
    dfList = []
    for i in range(1,374):
        # df = calculateDF_colorDvalue_method('img/image/'+ str(i) +'.jpg', 'img/image/'+ str(i+1) +'.jpg')
        Z = calculateDF_histgramBased_method('img/image/'+ str(i) +'.jpg', 'img/image/'+ str(i+1) +'.jpg')
        dfObject = { 'location' : i , 'df_value' : Z }
        dfList.append(dfObject)
        print '第' + str(i) + '个Z值为:' + str(Z)

    f = open('C:\\Users\\oliverfan\\PycharmProjects\\opencv\\frameDiff.txt', 'w')
    pickle.dump(dfList, f)
    f.close()


def fileTest():
    list = ['asdfsd' , 'adfsaf' , 'dasfsadf' , 'sdafaf']
    # d = dict(list = 'list')
    f = open('C:\\Users\\oliverfan\\PycharmProjects\\opencv\\file.txt', 'w')
    pickle.dump(list, f)
    f.close()

    f = open('C:\\Users\\oliverfan\\PycharmProjects\\opencv\\file.txt', 'r')
    d = pickle.load(f)
    print d
    f.close()


def main():
    # secenEdgeDetection()
    # secenEdgeListProcess()
    printt()

main()
