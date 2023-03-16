
import os
import upload_cloudinary
from datetime import datetime

directory = './timelapses'

#date_prefix = datetime.now().strftime("%Y-%m-%d")
date_prefix = '2023-03-14'

video_file_name = os.path.join(directory, f'timelapse_{date_prefix}.mp4')
upload_cloudinary.upload(video_file_name, f'timelapse_{date_prefix}')

