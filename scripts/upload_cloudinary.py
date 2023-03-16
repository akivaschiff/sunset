import sys
import os
import cloudinary
from cloudinary.uploader import upload, upload_large
from cloudinary.utils import cloudinary_url

def upload(local_file_path, remote_name):
    # Config
    cloudinary.config(
      cloud_name = "dzo9qayar",
      api_key = "241333354157767",
      api_secret = "Vw3cuMYeVhsmcaoBZ5bfEWsldds",
      secure = True
    )

    response = upload_large(local_file_path,
      folder = 'timelapses',
      resource_type = "video",
      public_id = remote_name,
      chunk_size = 6000000,
      eager_async = True,
    )
    return response['url']

if __name__ == '__main__':
    if not os.path.exists(sys.argv[1]):
        print('file does not exist')
        sys.exit(0)
    if len(sys.argv) != 3:
        print('wrong number of arguments, 2 required: <file_to_upload> <upload_name>')
        sys.exit(0)        
    print(f'uploading {sys.argv[1]} to {sys.argv[2]}')
    url = upload(sys.argv[1], sys.argv[2])
    print(f'file uploaded to: {url}')
