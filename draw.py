import cv2 as cv
import numpy as np
import os


IMAGES = 'images'
LABELS = 'labels'
OUTPUTS = 'outputs'
CLASSES = 'classes.txt'


classes = open(CLASSES).read().strip().split()
class_dic = dict()
for i, label in enumerate(classes):
    class_dic[i] = label
    
    
    
    
for im in os.listdir(IMAGES):
    txt = im.replace(im[-4:], '.txt')

    img = cv.imread(os.path.join(IMAGES, im))
    label = np.loadtxt(os.path.join(LABELS, txt)).tolist()
    height, width = img.shape[:2]


    if type(label[0]) == list:
        for obj in label:
            l = int(obj[0])
            w = round(obj[3]*width)
            h = round(obj[4]*height)
            x = round(obj[1]*width - w/2) # xmin
            y = round(obj[2]*height - h/2) # ymax
            cv.rectangle(img, (x, y), (x+w, y+h), (255,228,0), 1, cv.LINE_AA)
            cv.putText(img=img, text=class_dic[l], org=(x-2, y - 2), fontFace=1, fontScale=1, color=[255,255,255], lineType=cv.LINE_AA)

    else:
        obj = label
        l = int(obj[0])
        w = round(obj[3]*width)
        h = round(obj[4]*height)
        x = round(obj[1]*width - w/2)
        y = round(obj[2]*height - h/2)

        cv.rectangle(img, (x, y), (x+w, y+h), (255,228,0), 1, cv.LINE_AA)
        cv.putText(img=img, text=class_dic[l], org=(x-2, y - 2), fontFace=1, fontScale=1, color=[255,255,255], lineType=cv.LINE_AA)

    cv.imwrite(os.path.join(OUTPUTS,im), img)
    
print('Done')