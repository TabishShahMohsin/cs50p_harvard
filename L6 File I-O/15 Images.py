# Using binary files not only for textual info, but even for using photos and videos
# Using the famous pillow library
from PIL import Image
# Image with a capital I
# PIL all capital
import sys

images=[]

for arg in sys.argv[1:]:
    image=Image.open(arg)
    # print(image)
    images.append(image)
# print(images)

images[0].save(
    "costumes.gif", save_all=True, append_images= images[1:], duration=200, loop=0
)

#Use: python3 15\ Images.py Image1.png Image2.png Image3.png Image4.png