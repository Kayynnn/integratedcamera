import os
from PIL import Image
import math

path = './c2.png'

b = os.path.getsize(path)
print(b)

foo = Image.open(path)
x, y = foo.size
mult = 0.5
x2, y2 = math.floor(x*mult), math.floor(y*mult)
foo = foo.resize((x2,y2),Image.ANTIALIAS)
foo.save("1-1.png",quality=100)
