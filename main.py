from picamera2 import Picamera2, Preview
from libcamera import controls
import time

picam2 = Picamera2()

picam2.configure(picam2.still_configuration)
picam2.start_preview(Preview.NULL)

# set focus manually to infinity
# for some reason, autofocus doesn't work for me with no preview and stills capture
picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.0})

# wait one second
time.sleep(1)
picam2.start()

# Loop forever
while True:
    # Get the current time
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")

    # Take a picture and save it with the timestamp in the filename
    picam2.capture_file(f"images/image_{current_time}.jpg")

    # Wait for 30 seconds
    time.sleep(30)


picam2.stop_preview()
picam2.stop()