import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
from IPython.display import display
import numpy as np
path = "D:\\programming\\Python\\best.bmp"
img = Image.open(path)

sum = 0
for i in range(img.width):
    for j in range(img.height):
        x = img.getpixel((i,j))
        sum+=x[0]

print(sum)