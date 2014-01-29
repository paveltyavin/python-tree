import Image
import ImageDraw
from math import tanh

Size = 256

im = Image.new ( "RGB", ( Size, Size ), "#fff" )
draw = ImageDraw.Draw ( im )

def count(z):
    r = 0
    if z == 0: return 0
    while abs(z)<4:
        r += 1
        z = z*z + 0.29
    return r

for x in xrange(Size):
    for y in xrange(Size):
        z1 = (x+Size/0.8)*0.25/Size + (y-Size/1)*0.25/Size*1j
        c1 = int(255*tanh(0.02*count(z1)))
        z2 = (Size-x+Size/0.8)*0.25/Size + (Size-y-Size/1)*0.25/Size*1j
        c2 = int(255*tanh(0.02*count(z2)))
        draw.point((x,y),(c1,c2,70,255))

file_name = __file__[:-2]+'png'
im.save ( file_name )