from picamera2 import Picamera2, Preview
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

picam2 = Picamera2()

picam2.configure(picam2.still_configuration)
picam2.start_preview(Preview.NULL)
time.sleep(2)
picam2.start()
picam2.capture_file("capture.jpg")

picam2.stop_preview()
picam2.stop()