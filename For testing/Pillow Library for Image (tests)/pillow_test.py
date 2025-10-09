from PIL import Image
import requests
from io import BytesIO
filename = "resources/image1.png"
img = Image.open(filename)

# prints like the object
# print(img)

# rotates the image
img = img.rotate(angle=90, expand= True, fillcolor="green")

#shows the image in the default image app that you have in your machine
img.show()


# img = Image.open("resources/butterfly.jpg")
#SHOWS THE WIDTH AND THE HEIGHT
# print(img.width, img.height)
# img.show()

# Resize scale up by 2x with high-quality resampling
# img = img.resize(
#     (int(img.width * 2), int(img.height * 2)),
#     resample=Image.LANCZOS)

# print(img.width, img.height)
# img.show()