from PIL import Image
import requests
from io import BytesIO

url = input("Enter the URL: ")
#this downloads the url to bytes
response = requests.get(url)

#this changes the bytes using bytesio to an img object
img = Image.open(BytesIO(response.content))
img.show()