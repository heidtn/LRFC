import camera
import cannon
import numpy as np
import time

dart_cannon = cannon.Cannon()
cam = camera.CameraTracker(0, np.matrix([[700., 0., 640./2.], 
                                          [0.,  700., 480/2.], 
                                          [0.,   0., 1.]]))

pan, tilt, _ = cam.wait_for_event()
print "Pan: {}, tilt: {}".format(np.rad2deg(pan), np.rad2deg(tilt))
dart_cannon.set_pan_tilt(np.rad2deg(pan), 0.)
time.sleep(0.25)
dart_cannon.fire()