import cv2
import os
import sys
from datetime import datetime

date_prefix = datetime.now().strftime("%Y-%m-%d") if len(sys.argv) == 1 else sys.argv[1]

# create timelapse directory
directory = './timelapses'

if not os.path.exists(directory):
    os.makedirs(directory)

# specify the path to the folder containing the images
image_folder = './images'

# specify the desired frame rate of the output video
fps = 30.0

# get a list of all the image filenames in the folder
image_filenames = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg') and f > f'image_{date_prefix}_15-30'  and f < f'image_{date_prefix}_19-15']

# sort the image filenames in alphabetical order
image_filenames.sort()

if len(image_filenames) == 0:
	print('Could not find any images')
	sys.exit(0)

video_file_name = os.path.join(directory, f'{date_prefix}.mp4')
print(f'creating video from {len(image_filenames)} images at {video_file_name}')

# open the first image to get the image size
img = cv2.imread(image_filenames[0])
height, width, channels = img.shape

# create a video writer object with the specified frame rate and size
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # specify the codec for the output video
out = cv2.VideoWriter(video_file_name, fourcc, fps, (width, height))

# loop through each image in the folder and write it to the video
for image_filename in image_filenames:
    img = cv2.imread(image_filename)
    out.write(img)

# release the video writer and close all windows
out.release()
cv2.destroyAllWindows()