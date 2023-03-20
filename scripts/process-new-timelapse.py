import sys
import os
import upload_cloudinary
import create_video
from datetime import datetime

# create timelapse directory
directory = './timelapses'
image_folder = './images'

if not os.path.exists(directory):
    os.makedirs(directory)

# date_prefix = '2023-03-14'
date_prefix = datetime.now().strftime("%Y-%m-%d")

# get a list of all the image filenames in the folder
image_filenames = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if
                   f.endswith('.jpg') and f.startswith(f'image_{date_prefix}')]

# sort the image filenames in alphabetical order
image_filenames.sort()

if len(image_filenames) == 0:
    print('Could not find any images')
    sys.exit(0)

video_file_name = os.path.join(directory, f'timelapse_{date_prefix}.mp4')

print(f'creating video from {len(image_filenames)} images at {video_file_name}')
create_video.create_video(image_filenames, video_file_name)
print('finished creating video. uploading...')
url = upload_cloudinary.upload(video_file_name, f'timelapse_{date_prefix}')
print(f'file uploaded successfully to: {url}')
