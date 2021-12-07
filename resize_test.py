from PIL import Image
import math

foo = Image.open("1.png")
x, y = foo.size
mult = 0.3
x2, y2 = math.floor(x*mult), math.floor(y*mult)
foo = foo.resize((x2,y2),Image.ANTIALIAS)
foo.save("1-1.png",quality=100)
