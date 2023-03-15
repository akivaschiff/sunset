from picamera2 import Picamera2, Preview
from libcamera import controls
import time

picam2 = ''

def init():
	global picam2
	picam2 = Picamera2()

	# picam2.configure(picam2.still_configuration) - swapped this for the following line where I can control the size
	picam2.configure(picam2.create_still_configuration(main={"size": (1920, 1080)}))
	picam2.start_preview(Preview.NULL)

	# set focus manually to infinity
	# for some reason, autofocus doesn't work for me with no preview and stills capture
	picam2.set_controls({ "AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.0 })

	# wait one second
	time.sleep(1)
	picam2.start()

def capture(filename):
	global picam2
    picam2.capture_file(filename)

def destroy():
	global picam2
	picam2.stop_preview()
	picam2.stop()
