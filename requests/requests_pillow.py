# import requests and io library
import requests
from io import BytesIO
# import Image from the pillow library  : pip3 install pillow
from PIL import Image

# get an image from url
r = requests.get("https://wallpapercave.com/wp/PMEVE7F.jpg")

print("Status Code:", r.status_code)

# creates a image using the binary content that has been returned
# uses io package to parse the binary
image = Image.open(BytesIO(r.content))

# prints image properties
print(image.size, image.format, image.mode)
# create path variable
path = "./image." + image.format

# try except method to save image using the path and image format (JPG, PNG)
try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")