from datetime import datetime
import time
import importlib  
import sys
import intervaler

testMode = 'test' in sys.argv
camera = importlib.import_module('camera-test' if testMode else 'camera') 

camera.init()
while True:

    # Get the current time
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    # Take a picture and save it with the timestamp in the filename
    camera.capture(f"images/image_{current_time}.jpg")

    # Sleep till next image
    seconds_to_wait = intervaler.getInterval(datetime.now())
    if testMode:
    	print(f"waiting {seconds_to_wait} seconds till next picture")
    time.sleep(seconds_to_wait)

camera.destroy()
