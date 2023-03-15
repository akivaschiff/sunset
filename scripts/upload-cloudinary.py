import sys
import os
import cloudinary
from cloudinary.uploader import upload, upload_large
from cloudinary.utils import cloudinary_url

date_prefix = datetime.now().strftime("%Y-%m-%d") if len(sys.argv) == 1 else sys.argv[1]

directory = './timelapses'

video_file_name = os.path.join(directory, f'{date_prefix}.mp4')

# Config
cloudinary.config(
  cloud_name = "dzo9qayar",
  api_key = "241333354157767",
  api_secret = "Vw3cuMYeVhsmcaoBZ5bfEWsldds",
  secure = True
)

print(f'uploading {video_file_name}')

response = upload_large(video_file_name, 
  resource_type = "video",
  public_id = f'timelapse_{date_prefix}',
  chunk_size = 6000000,
  eager_async = True,
)

print(response['url'])
print(response['public_url'])
