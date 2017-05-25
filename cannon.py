import cv2
import maestro

PAN_CENTER = 90.
TILT_CENTER = 90.
TRIGGER_CENTER = 45.

TRIGGER_FIRE = 10.

PAN     = 0
TILT    = 1
TRIGGER = 2

class Cannon():
    def __init__(self, port='/dev/ttyACM0'):
        self.usb_controller = maestro.Controller(port)
        self.ready_position()
    
    def ready_position(self):
        self.set_angle(PAN, PAN_CENTER)
        self.set_angle(TILT, TILT_CENTER)
        self.set_angle(TRIGGER, TRIGGER_CENTER)

    def fire(self):
        self.set_angle(TRIGGER, TRIGGER_FIRE)

    def set_angle(self, servo, angle):
        # takes a servo number (0-n) and an angle in degrees (-90 - 90)
        ms = 1500 + (angle*1500./90.)
        quarter_ms = ms*4
        quarter_ms = int(quarter_ms + .5)
        self.servoController.setTarget(servo, quarter_ms)
        print("set servo", servo, "to", angle)