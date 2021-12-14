import numpy as np
import cv2

def line_detection(frame2scan_left, frame2scan_right):
    # --- Line detection --- #
    gray_left = cv2.cvtColor(frame2scan_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(frame2scan_right, cv2.COLOR_BGR2GRAY)

    kernel_size = 5
    blur_gray_left = cv2.GaussianBlur(gray_left, (kernel_size, kernel_size), 0)
    blur_gray_right = cv2.GaussianBlur(gray_right, (kernel_size, kernel_size), 0)

    low_threshold = 50
    high_threshold = 100
    edges_left = cv2.Canny(blur_gray_left, low_threshold, high_threshold)
    edges_right = cv2.Canny(blur_gray_right, low_threshold, high_threshold)

    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 100  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 200  # minimum number of pixels making up a line
    max_line_gap = 25  # maximum gap in pixels between connectable line segments
    line_image_left = np.copy(frame2scan_left) * 0  # creating a blank to draw lines on
    line_image_right = np.copy(frame2scan_right) * 0  # creating a blank to draw lines on

    # Run Hough on Edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines_left = cv2.HoughLinesP(edges_left, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

    lines_right = cv2.HoughLinesP(edges_right, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

    if lines_left is not None:
        for line in lines_left:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image_left, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Draw the lines on the  image
        lines_edges_left = cv2.addWeighted(frame2scan_left, 1, line_image_left, 1, 1)
    else:
        lines_edges_left = frame2scan_left

    if lines_right is not None:
        for line in lines_right:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image_right, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Draw the lines on the  image
        lines_edges_right = cv2.addWeighted(frame2scan_right, 1, line_image_right, 1, 1)
    else:
        lines_edges_right = frame2scan_right

    return lines_edges_left, lines_edges_right
