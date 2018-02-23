# coding=utf-8
from sys import argv, exit
import cv2
import  numpy as np

def changeBackground(img, img_back, zoom_size, center):
    # 日常缩放
    rows, cols, channels = img_back.shape
    #img_back = cv2.resize(img_back, None, fx=0.7, fy=0.7)
    #cv2.imshow('img_back', img_back)

    rows, cols, channels = img.shape
    #img = cv2.resize(img, None, fx=0.4, fy=0.4)
    img = cv2.resize(img, zoom_size)
    #cv2.imshow('img', img)
    rows, cols, channels = img.shape  # rows，cols最后一定要是前景图片的，后面遍历图片需要用到
    #print rows, cols

    # 转换hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 获取mask
    lower_blue = np.array([78, 43, 46])
    upper_blue = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #cv2.imshow('Mask', mask)

    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    #cv2.imshow('erode', erode)
    dilate = cv2.dilate(erode, None, iterations=1)
    #cv2.imshow('dilate', dilate)

    #print img.shape
    #print img_back.shape
    # 遍历替换
    #center = [50, 50]  # 在新背景图片中的位置
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 0:  # 0代表黑色的点
                img_back[center[0] + i, center[1] + j] = img[i, j]  # 此处替换颜色，为BGR通道
    #cv2.imshow('res', img_back)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return img_back


if __name__ == '__main__':
    img = cv2.imread('head.jpg')
    img_back = cv2.imread('empty.png')
    zoom_size = (500, 670)
    center = (690, 1500)
    changeBackground(img, img_back, zoom_size, center)
