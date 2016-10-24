#! /usr/bin python
# -*- coding:utf-8 -*-

import sys
import re
from PIL import Image

'''ascii = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!;:,\^`'.")'''
ascii = list('@%#S?*+:,. ')

def getdata(r,g,b):

	length = len(ascii)
	pi = int(0.2126*r + 0.7152*g + 0.0722*b)
	if pi == 0:
		return ''
	unit = (256.0)/length
	return ascii[int(pi/unit)]

img = Image.open(sys.argv[1])
w = img.size[0]
h = img.size[1]
'''h = int(h *0.6)'''
w = int(w * 0.5)
h = int(h * 0.3)
img = img.resize((w,h),Image.NEAREST)

output = ''

for y in range(h):
	for o in range(w):
		output += getdata(*img.getpixel((o,y)))
	output += '\n'

f = open('11.txt','w')
f.write(output)
f.close()