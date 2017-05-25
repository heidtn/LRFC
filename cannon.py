import cv2
import maestro
import time

PAN_CENTER = 0.
TILT_CENTER = 30.
TRIGGER_CENTER = 20.

TRIGGER_FIRE = 10.

PAN     = 0
TILT    = 1
TRIGGER = 2

class Cannon():
    def __init__(self, port='/dev/ttyACM0'):
        self.usb_controller = None
        try:
            self.usb_controller = maestro.Controller(port)
        except Exception:
            raise Exception("couldn't open usb controller!")
        self.ready_position()

    def __del__(self):
        if self.usb_controller is not None:
            self.usb_controller.close()
    
    def ready_position(self):
        self.set_angle(PAN, PAN_CENTER)
        self.set_angle(TILT, TILT_CENTER)
        self.set_angle(TRIGGER, TRIGGER_CENTER)

    def fire(self):
        self.set_angle(TRIGGER, TRIGGER_FIRE)
        time.sleep(0.5)
        self.set_angle(TRIGGER, TRIGGER_CENTER)

    def set_pan_tilt(self, pan, tilt):
        self.set_angle(PAN, pan)
        self.set_angle(TILT, tilt)

    def set_angle(self, servo, angle):
        # takes a servo number (0-n) and an angle in degrees (-90 - 90)
        ms = 1500 + (angle*1500./90.)
        quarter_ms = ms*4
        quarter_ms = int(quarter_ms + .5)
        self.usb_controller.setTarget(servo, quarter_ms)
        print("set servo", servo, "to", angle)