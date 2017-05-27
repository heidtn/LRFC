import cv2
import time
import numpy as np


CONTOUR_SIZE_THRESH = 100
DIFF_THRESH = 30


class CameraTracker():
    def __init__(self, source, intrinsic_matrix):
        self.cap = None
        self.cap = cv2.VideoCapture(source)
        self.intrinsic_matrix = intrinsic_matrix

    def __del__(self):
        self.cap.release()

    def wait_for_event(self, display=True):
        while True:
            ret, frame1 = self.cap.read()
            time.sleep(0.1)
            ret, frame2 = self.cap.read()

            gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            gray1 = cv2.GaussianBlur(gray1, (5, 5), 0)
            gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)


            pan, tilt, img = check_for_movement(gray1, gray2)
            if pan is not None:
                return pan, tilt, img


    def check_for_movement(self, image1, image2):
        diff = np.abs(image1 - image2)

        diff[diff < DIFF_THRESH] = 0
        diff[diff > 0] = 255

        img, contours, hierarchy = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) > CONTOUR_SIZE_THRESH:
                M = cv2.moments(cnt)
                cX = M["m10"] / M["m00"]
                cY = M["m01"] / M["m00"]
                pixel_homogenous = np.matrix([cX, cY, 1]).T
                ray = self.intrinsic_matrix.T * pixel_homogenous
                tilt = np.arctan2(ray[1], ray[2])
                pan = np.arctan2(ray[0], ray[2])

                img = cv2.circle(gray2, (cX, cY), 4, (0, 255, 0), 4)
                return pan, tilt, img
            else:
                return None, None, img
                    

