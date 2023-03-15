import time
import importlib  
import sys

moduleName = 'camera-test' if sys.argv[-1] == 'test' else 'camera'
camera = importlib.import_module(moduleName) 

camera.init()
while True:
    # Get the current time
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")

    # Take a picture and save it with the timestamp in the filename
    camera.capture(f"images/image_{current_time}.jpg")

    # Wait for 30 seconds
    time.sleep(30)

camera.destroy()
