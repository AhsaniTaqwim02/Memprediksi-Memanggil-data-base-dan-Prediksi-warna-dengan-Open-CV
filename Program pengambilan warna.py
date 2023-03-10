import cv2
import numpy as np
import csv
import time

from sklearn import svm
import pandas as pd

cap = cv2.ViedoCapture(1)
img = cap.set(cv2.CAP_PROF_FRAME_WIDTH,480)
img = cap.set(cv2.CAP_PROF-FRAME-HEIGHT,480)

#Database: Gerbang logika and
#membaca data dari file
FileDB = 'warna.txt'
Database = pd.read_csv(FileDB, sep=",",header=0)
print(Database)

#x = Data, y = Target
x = Database[[u'B',u'G',u'R']]
y = Database.Target

clf = svm.SCV()
clf.fit(x,y)

fpsLimit = 1
startTime= time.time()

while True:
    ret,img = cap.read()
    img = cv2.flip(img,1)
    for x in range (330,340,1):
        for y in range (220,260,1):
            color = img [x.y]
            colorB = img [y,x,0]
            colorG = img [y,x,1]
            colorR = img [y,x,2]

    print('B G R =', color)
    cv2.imshow("Color Tracking",img)

    if clf.predict([color]) == 'biru':
        print ("Biru")

    elif clf.predict([color]) == 'hijau':
        print ("Hijau")

    elif clf.predict([color]) == 'kuning':
        print ("Kuning")

    elif clf.predict([color]) == 'merah':
        print ("Merah")

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.relase()
cv2.destroyAllWindows()
