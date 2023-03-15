import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

# Config
cloudinary.config(
  cloud_name = "dzo9qayar",
  api_key = "241333354157767",
  api_secret = "Vw3cuMYeVhsmcaoBZ5bfEWsldds",
  secure = True
)

# Upload
upload("./images/results-storm/image_2023-03-13_18-51-47.jpg", public_id="test_image")

# Transform
url, options = cloudinary_url("test_image")

print(url)
print(options)