import sys

import cloudinary
from cloudinary.uploader import upload
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

# Upload
upload(video_file_name, public_id=f'timelapse_{date_prefix}')

# Transform
url, options = cloudinary_url('timelapse_{date_prefix}')

print(url)
print(options)