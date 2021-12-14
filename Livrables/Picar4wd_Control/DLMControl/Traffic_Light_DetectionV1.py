import numpy as np
import cv2
from PIL.Image import *

# source : https://perso.ensta-paris.fr/~pcarpent/MO102/Cours/Projets/Pr-vision.pdf
# https://stackoverflow.com/questions/11386556/converting-an-opencv-bgr-8-bit-image-to-cie-lab
# https://www.researchgate.net/publication/230601628_Traffic_Lights_Detection_in_Adverse_Conditions_Using_Color_Symmetry_and_Spatiotemporal_Information
# rgb2lab : https://gist.github.com/bikz05/6fd21c812ef6ebac66e1
# Get BGR color of each pixel : https://stackoverflow.com/questions/12187354/get-rgb-value-opencv-python

def traffic_light_detection(frame2scan_top):
    # --- Color space conversion --- #
    dst = find_rect(frame2scan_top)
    # dst = find_circle(rect_frame)

    return dst

def find_circle(rect_frame):
    gray = cv2.cvtColor(rect_frame, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray, (9, 9), 2, 2)
    circles = cv2.HoughCircles(gauss, cv2.HOUGH_GRADIENT, 2.0, 20, 50, 30, 100)
    count_circle = 0
    TLcolor=""
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        c_cercle_x = {'x1': 0, 'x2': 0, 'x3': 0}
        c_cercle_y = {'y1': 0, 'y2': 0, 'y3': 0}
        if len(circles) == 3:
            # print(rect_frame.shape)
            try:
                for (x, y, r) in circles:
                    count_circle += 1
                    c_cercle_x['x' + str(count_circle)] = x
                    c_cercle_y['y' + str(count_circle)] = y
                    # draw the circle in the output image, then draw a rectangle
                    # corresponding to the center of the circle
                    cv2.circle(rect_frame, (x, y), r, (0, 255, 0), 4)
            except TypeError:
                count_circle += 1
                pass

            try:
                cercle_rouge = min(c_cercle_y, key=c_cercle_y.get)
                cercle_vert = max(c_cercle_y, key=c_cercle_y.get)

                _, _, R = rect_frame[c_cercle_y[cercle_rouge], c_cercle_x['x1']]
                _, G, _ = rect_frame[c_cercle_y[cercle_vert], c_cercle_x['x1']]
                print("Rouge: ", R, " | Vert: ", G)
                if (R >= 130 and G < R):
                    cv2.putText(rect_frame, "R", (c_cercle_x['x1'], c_cercle_y[cercle_rouge]),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (255, 0, 0))
                    TLcolor = "red"
                if (G >= 130 and R < G):
                    cv2.putText(rect_frame, "V", (c_cercle_x['x1'], c_cercle_y[cercle_vert]),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (255, 0, 0))
                    TLcolor = "green"
            except IndexError:
                pass

    return rect_frame, count_circle, TLcolor

def find_rect(frame2scan_top):
    hsv_frame = cv2.cvtColor(frame2scan_top, cv2.COLOR_BGR2HSV)  # tranform it to LAB
    h, s, v = cv2.split(hsv_frame)
    v[v <= 0] = 0
    v[v > 50] = 0
    TLdetected = False
    TLcolor = ""

    ## normalize, do the open-morp-op
    normed = cv2.normalize(v, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
    kernel = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(3, 3))
    opened = cv2.morphologyEx(normed, cv2.MORPH_OPEN, kernel)
    np.hstack((v, normed, opened))

    (contours, _) = cv2.findContours(opened, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    bboxes = []
    rboxes = []
    cnts = []
    dst = frame2scan_top.copy()
    i = 0

    for cnt in contours:
        i = i + 50
        ## Get the stright bounding rect
        bbox = cv2.boundingRect(cnt)
        x, y, w, h = bbox
        if w < 150 and h < 2 * w:
            continue

        ## Draw rect
        circle, nb_circle, TLcolor = find_circle(dst[y: y + h, x: x + w])
        if nb_circle == 3:
            cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 2, 16)
            TLdetected = True

        ## Get the rotated rect
        rbox = cv2.minAreaRect(cnt)

        ## backup
        bboxes.append(bbox)
        rboxes.append(rbox)
        cnts.append(cnt)

    return dst, TLdetected, TLcolor

    # l_channel, a_channel, b_channel = cv2.split(ciel_frame.copy())
        # RGYB_frame = np.zeros([ciel_frame.shape[0], ciel_frame.shape[1], 3])
        # # RGYB_frame = np.zeros([ciel_frame.shape[0], ciel_frame.shape[1]])
        # YB_frame = np.zeros([ciel_frame.shape[0], ciel_frame.shape[1]])
        # RG_frame = np.zeros([ciel_frame.shape[0], ciel_frame.shape[1]])
        # for i in range(ciel_frame.shape[0]):
        #     for y in range(ciel_frame.shape[1]):
        #         l_channel_cur = l_channel[i][y] / 255 * 100
        #         a_channel_cur = a_channel[i][y] - 128
        #         b_channel_cur = b_channel[i][y] - 128
        #         RG_frame[i][y] = (l_channel_cur * a_channel_cur)
        #         YB_frame[i][y] = (l_channel_cur * b_channel_cur)
        #         RGYB_frame[i][y] = (l_channel_cur * (a_channel_cur + b_channel_cur))

        # # --- RGB2LAB --- #
        # def func(t):
        #     if (t > 0.008856):
        #         return np.power(t, 1 / 3.0)
        #     else:
        #         return 7.787 * t + 16 / 116.0
        #
        # # Conversion Matrix
        # matrix = [[0.412453, 0.357580, 0.180423],
        #           [0.212671, 0.715160, 0.072169],
        #           [0.019334, 0.119193, 0.950227]]
        #
        # lab_frame = np.zeros([frame2scan_top.shape[0], frame2scan_top.shape[1]])
        # for x in range(frame2scan_top.shape[0]):
        #     for y in range(frame2scan_top.shape[1]):
        #         B = frame2scan_top[x, y, 0]
        #         G = frame2scan_top[x, y, 1]
        #         R = frame2scan_top[x, y, 2]
        #
        #         print("Pixel[", x, ", ", y, "] = ", "B:", B, "G:", G, "R:", R)
        #
        #         # RGB values lie between 0 to 1.0
        #         rgb = [R/255, G/255, B/255]  # RGB
        #
        #         cie = np.dot(matrix, rgb)
        #
        #         cie[0] = cie[0] / 0.950456
        #         cie[2] = cie[2] / 1.088754
        #
        #         # Calculate the L
        #         L = 116 * np.power(cie[1], 1 / 3.0) - 16.0 if cie[1] > 0.008856 else 903.3 * cie[1]
        #
        #         # Calculate the a
        #         a = 500 * (func(cie[0]) - func(cie[1]))
        #
        #         # Calculate the b
        #         b = 200 * (func(cie[1]) - func(cie[2]))
        #
        #         #  Values lie between -128 < b <= 127, -128 < a <= 127, 0 <= L <= 100
        #         Lab = [L, a, b]
        #         print(Lab)
        #
        #
        #         lab_frame[x, y] = L * (a + b)

        # return RG_frame, YB_frame, RGYB_frame
