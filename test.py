from sys import argv, exit
import os
import cv2
from functools import partial
import numpy as np
import glob
from multiprocessing import Pool
from PIL import Image, ImageChops


def removeBackground(image_file, out_folder):
    img = cv2.imread(image_file)

    # Crop out white borders from image so the edge detection algorithm doesnt detect the border as an edge
    im = Image.fromarray(img)
    bg = Image.new(im.mode, im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        im = im.crop(bbox)
        img = np.array(im)

    height, width, _ = img.shape

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Calculate otsu threshold for edge detection
    ret, threshed_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    high = ret
    low = high * 0.5

    # Edge detection
    edges = cv2.Canny(gray, low, high)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    # Find all contours and get the one with the biggest area
    _, contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    max_contour = sorted(contours, key=lambda c: cv2.contourArea(c), reverse=True)[0]
    x, y, w, h = cv2.boundingRect(max_contour)

    # Add a 5px buffer to bounding box
    x1 = x if x - 0 > 5 else 5
    x2 = x + w if abs(width - (x + w)) > 5 else (x + w) - 5
    y1 = y if y - 0 > 5 else 5
    y2 = y + h if abs(height - (y + h)) > 5 else (y + h) - 5

    # Create bounding box based on the largest contour of the image
    rect = (x1, y1, x2, y2)

    mask = np.zeros(img.shape[:2], dtype=np.uint8)

    # Dummy placeholders
    bgdmodel = np.zeros((1, 65), np.float64)
    fgdmodel = np.zeros((1, 65), np.float64)

    # Iteratively extract foreground object from background
    cv2.grabCut(img, mask, rect, bgdmodel, fgdmodel, 10, cv2.GC_INIT_WITH_RECT)
    cv2.grabCut(img, mask, rect, bgdmodel, fgdmodel, 10, cv2.GC_INIT_WITH_MASK)

    # Remove background from image
    mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')
    output = cv2.bitwise_and(img, img, mask=mask2)

    # Convert black background to white
    output[np.where((output == [0, 0, 0]).all(axis=2))] = [255, 255, 255]
    cv2.imwrite(os.path.join(out_folder, os.path.basename('out_'+image_file)), output)


def main(in_folder, out_folder):
    file_types = ['*.jpg', '*.jpeg', '*.png']
    images = []
    for file_type in file_types:
        images.extend(glob.glob('%s/%s' % (in_folder, file_type)))
    p = Pool(processes=16)
    p.map(partial(removeBackground, out_folder=out_folder), images)


if __name__ == '__main__':
    try:
        in_image = argv[1]
        out_image = argv[2]
        # if not os.path.exists(out_folder):
        #	os.makedirs(out_folder)
    except:
        print "Provide the following arguments"
        print "1. Input image filename"
        print "2. Output image filename"
        exit()
    #main(in_image, out_image)
    removeBackground(in_image, '.')
