import cv2
import os

# specify the path to the folder containing the images
image_folder = '/Users/akivaschiff/myprojects/sunset/images/results-storm'

# specify the desired frame rate of the output video
fps = 30.0

# get a list of all the image filenames in the folder
image_filenames = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg') and f[:len('image_2023-03-14_16-16-54')] >= 'image_2023-03-14_16-16-54']

# sort the image filenames in alphabetical order
image_filenames.sort()

# open the first image to get the image size
img = cv2.imread(image_filenames[0])
height, width, channels = img.shape

# create a video writer object with the specified frame rate and size
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # specify the codec for the output video
out = cv2.VideoWriter('/Users/akivaschiff/myprojects/sunset/output-storm-small.mp4', fourcc, fps, (width, height))

# loop through each image in the folder and write it to the video
for image_filename in image_filenames:
    img = cv2.imread(image_filename)
    out.write(img)

# release the video writer and close all windows
out.release()
cv2.destroyAllWindows()