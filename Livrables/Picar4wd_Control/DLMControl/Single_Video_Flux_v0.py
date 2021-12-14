import cv2
import threading
import numpy as np
import Object_Detection
import Traffic_Light_Detection
import Line_Detection
import Color_Detection

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    #cv2.CAP_V4L
    cam = cv2.VideoCapture(0,cv2.CAP_V4L) #Linux
    #cam = cv2.VideoCapture(camID) Windows
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
        classe, colors, net = Object_Detection.init_model()
    else:
        rval = False

    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()

        # affichage du flux vidéo dans une fenetre
        cv2.namedWindow("Result_" + str(camID))
        cv2.imshow("Result_" + str(camID), frame)
        # --- Exit the Video --- #
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)

thread1 = camThread("Camera 1", 1)
thread1.start()
