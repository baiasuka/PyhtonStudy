# coding:utf-8
import sys

import cv2
# 待检测的图片路径
for i in range(0,19):
    imagepath = "./face_img/avatar%s.jpg" %(i)

    # 获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值
    face_cascade = cv2.CascadeClassifier(r'./classifier/haarcascade_frontalface_alt_tree.xml')

    # 读取图片
    image = cv2.imread(imagepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 探测图片中的人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    print("发现{0}个人脸!".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 3)

        # cv2.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2)
    if len(faces)>0:
        cv2.imwrite("./face_check_result_alt_tree/avatar%sexisted.png" % (i), image)
    else:
        cv2.imwrite("./face_check_result_alt_tree/avatar%s.png" % (i), image)
    print("create%s" % (i))