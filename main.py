from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()

picam2.configure(picam2.still_configuration)
picam2.start_preview(Preview.NULL)
time.sleep(2)
picam2.start()

# Loop forever
while True:
    # Get the current time
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")

    # Take a picture and save it with the timestamp in the filename
    picam2.capture_file(f"images/image_{current_time}.jpg")

    # Wait for 2 minutes
    time.sleep(120)


picam2.stop_preview()
picam2.stop()