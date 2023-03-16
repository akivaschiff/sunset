
import os
import upload_cloudinary
from datetime import datetime


# create timelapse directory
directory = './timelapses'

if not os.path.exists(directory):
    os.makedirs(directory)


#date_prefix = datetime.now().strftime("%Y-%m-%d")
date_prefix = '2023-03-14'

video_file_name = os.path.join(directory, f'timelapse_{date_prefix}.mp4')
upload_cloudinary.upload(video_file_name, f'timelapse_{date_prefix}')




def get_images():
	date_prefix = datetime.now().strftime("%Y-%m-%d") if len(sys.argv) == 1 else sys.argv[1]
	# specify the path to the folder containing the images
	image_folder = './images'

	# get a list of all the image filenames in the folder
	image_filenames = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg') and f > f'image_{date_prefix}_15-30'  and f < f'image_{date_prefix}_19-15']

	# sort the image filenames in alphabetical order
	image_filenames.sort()

	if len(image_filenames) == 0:
		print('Could not find any images')
		sys.exit(0)

	video_file_name = os.path.join(directory, f'{date_prefix}.mp4')