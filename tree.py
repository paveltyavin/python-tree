#!/usr/bin/env python
import random
import Image
import ImageDraw
import math

Size = 512

im = Image.new ( "RGBA", ( Size, Size ), "#fff" )
draw = ImageDraw.Draw ( im )

xc = Size/2
yc = Size/2
pi = math.pi

p_sex = 0.7
k_dec = 0.95
N = 30
beta = 8.0/N
N_der = 10
l_0 = (1-k_dec)*0.7*Size/ N_der * 2

def mix_colors(c_1,c_2, p):
    c = ()
    for i in xrange(3):
        c += (int(c_1[i] + p * (c_2[i] - c_1[i])),)
    return c

sky_2 = (194, 218, 255)
sky_1 = (204, 220, 255)

for y in xrange(int(Size*.5)):
    draw.line(((0,y),(Size,y)),mix_colors(sky_1, sky_2, 2.0*y/Size))

ground_2 = (40, 112, 60)
ground_1 = (67, 184, 100)

for y in xrange(int(Size*.5)):
    draw.line(((0,y+Size/2),(Size,y+Size/2)), mix_colors( ground_1, ground_2, 2.0*y/Size))

tree_2 = (100,200,100)
tree_1 = (148,64,18)

R_1 = 0
R_2 = 255
G_1 = 0
G_2 = 255
B_1 = 0
B_2 = 255

def tr(x,y,a, l, n):
    xn = x + l*math.cos(a)
    yn = y + l*math.sin(a)
    R = int(R_1 + 1.0*n/N * (R_2 - R_1))
    G = int(G_1 + 1.0*n/N * (G_2 - G_1))
    B = int(B_1 + 1.0*n/N * (B_2 - B_1))
    w = int( 0.02*Size * (1.0*n/N)**5 + 1)
    tree = mix_colors(tree_2, tree_1, 1.0*n/N)
    if n > 0:
        if random.random()> p_sex:
            tr (xn, yn, a-beta, l*k_dec, n-1)
            tr (xn, yn, a+beta, l*k_dec, n-1)
        else:
            tr (xn, yn, a, l*k_dec, n-1)
    if abs(a-pi/2)<pi:
        draw.line( ( (x+xc, -y+yc), (xn+xc, -yn+yc )), tree , width = w)

for y in xrange(int(Size*0.1), int(Size*0.5),int(Size*0.07)):
    for x in xrange(int(-Size*0.5), int(Size *0.4), int(Size/N_der)):
        l = 1.5*l_0 *random.randrange(7,12)/10 * (Size*0.5/(Size*0.6-y))
        tr(x + random.randint(0,int(Size/N_der)) , -y + random.randint(0,int(Size*.1)), pi*0.5, l , N)

file_name = __file__[:-2]+'png'
im.save ( file_name )
im.show()