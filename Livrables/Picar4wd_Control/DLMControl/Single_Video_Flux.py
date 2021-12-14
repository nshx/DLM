import cv2
import threading
import numpy as np
import Color_Detection
import Line_Detection
import Traffic_Light_Detection
import Object_Detection
from DLMControlLib import DLMControl as DLMC

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
    cam = cv2.VideoCapture(camID,cv2.CAP_V4L)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
        classe, colors, net = Object_Detection.init_model()
    else:
        rval = False
    DLMcontrol = DLMC.DLMControl()
    DLMcontrol.threadStart()

    while rval:
        #cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        # --- Split frame --- #
        height = frame.shape[1]
        width = frame.shape[0]

        frame2scan_left = frame[0:width, 0:int(height * .3)]
        frame2scan_middle = frame[0:width, int(height * .3):int(height * .7)]
        frame2scan_right = frame[0:width, int(height * .7):height]

        # --- Operations on the Frame --- #
        frame2scan_left, frame2scan_right = Line_Detection.line_detection(frame2scan_left, frame2scan_right)
        frame2scan_middle = Object_Detection.object_detection(frame2scan_middle, camID, classe, colors, net)

        # --- Regroupement de la frame pour le résultat --- #
        result_frame = np.concatenate((frame2scan_left, frame2scan_middle, frame2scan_right), 1)
        #frame2scan_top = result_frame[0:int(width * .3), 0:height]
        #frame2scan_bot = result_frame[int(width * .3):width, 0:height]
        result_frame, TLdetected, TLcolor = Traffic_Light_Detection.traffic_light_detection(result_frame)
        if (TLdetected == True):
                print("LOG: Traffic light detected")
                DLMcontrol.sig_TLdetected(TLcolor)
                
                
        
        #result_frame = np.concatenate((cielab_frame, frame2scan_bot), 0)
        # affichage du flux vidéo dans une fenetre
        cv2.namedWindow("Result_" + str(camID))
        cv2.imshow("Result_" + str(camID), result_frame)
        # --- Exit the Video --- #
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)

thread1 = camThread("Camera 1", 0)
thread1.start()
