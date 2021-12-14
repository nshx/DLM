# python3 Object_Detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

# importer tout les packages requis
#from imutils.video import VideoStream
#from imutils.video import FPS
import numpy as np
#import imutils
import time
import cv2

def init_model():
    # initialiser la liste des objets entrainés par MobileNet SSD
    # création du contour de détection avec une couleur attribuée au hasard pour chaque objet
    CLASSES = ["", "", "velo", "", "",
               "", "autobus", "voiture", "chat", "", "", "",
               "chien", "cheval", "moto", "personne", "", "",
               "", "", ""]

    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

    # chargement des fichiers depuis le répertoire de stockage
    print(" ...Chargement du modèle...")
    net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt",
                                   "MobileNetSSD_deploy.caffemodel")
    return CLASSES, COLORS, net

def object_detection(frame, id, CLASSES, COLORS, net):
    # récupération du flux vidéo, redimension
    # afin d'afficher au maximum 800 pixels
    #frame_cpy = imutils.resize(frame, width=800)
    frame_cpy = frame.copy()

    # récupération des dimensions et transformation en collection d'images
    (h, w) = frame_cpy.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame_cpy, (300, 300)),
                                 0.007843, (300, 300), 127.5)

    # determiner la détection et la prédiction
    net.setInput(blob)
    detections = net.forward()

    # boucle de détection
    for i in np.arange(0, detections.shape[2]):
        # calcul de la probabilité de l'objet détecté
        # en fonction de la prédiction
        confidence = detections[0, 0, i, 2]

        # supprimer les détections faibles
        # inférieures à la probabilité minimale
        if confidence > 0.2:
            # extraire l'index du type d'objet détecté
            # calcul des coordonnées de la fenêtre de détection
            idx = int(detections[0, 0, i, 1])
            if CLASSES[idx] != "":
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # creation du contour autour de l'objet détecté
                # insertion de la prédiction de l'objet détecté
                label = "{}: {:.2f}%".format(CLASSES[idx],
                                             confidence * 100)
                cv2.rectangle(frame_cpy, (startX, startY), (endX, endY),
                              COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame_cpy, label, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

        return frame_cpy
