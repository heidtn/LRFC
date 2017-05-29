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

    def wait_for_event(self, display=True, lead=False):
        while True:
            ret, frame1 = self.cap.read()
            time.sleep(0.1)
            ret, frame2 = self.cap.read()

            gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            gray1 = cv2.GaussianBlur(gray1, (5, 5), 0)
            gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)

            pan, tilt, img = self.check_for_movement(gray1, gray2)

            if display:
                cv2.imshow('frame', img)
                cv2.waitKey(0)
            if pan is not None:
                return pan, tilt, img


    def check_for_movement(self, image1, image2):
        diff = cv2.absdiff(image2, image1)
        height, width = image1.shape

        diff[diff < DIFF_THRESH] = 0
        diff[diff > 0] = 255

        found_good_contour = False
        avg_x = 0.
        avg_y = 0.
        count = 0

        img, contours, hierarchy = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) > CONTOUR_SIZE_THRESH:
                M = cv2.moments(cnt)
                cX = M["m10"] / M["m00"]
                cY = M["m01"] / M["m00"]
                avg_y += cY
                avg_x += cX
                count += 1
                found_good_contour = True
        
        if found_good_contour:
            avg_x /= count
            avg_y /= count

            cX = avg_x - self.intrinsic_matrix[0, 2]
            cY = self.intrinsic_matrix[1, 2] - avg_y
            f = self.intrinsic_matrix[0, 0]

            tilt = np.arctan2(cY, f)
            pan = np.arctan2(cX, f)

            diff = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
            diff = cv2.circle(diff, (int(avg_x), int(avg_y)), 4, (0, 255, 0), 4)
            return pan, tilt, diff

        return None, None, image1
                    

if __name__ == "__main__":
    tracker = CameraTracker("/home/brizo/Videos/Webcam/2017-05-29-135756.webm", np.matrix([[600., 0., 256./2], 
                                          [0.,  600, 192/2.], 
                                          [0.,   0., 1.]]))
    tracker.wait_for_event()
    cv2.waitKey(0)
