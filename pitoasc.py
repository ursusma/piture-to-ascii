#! /usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
import sys

ascii = "   ...',;:clodxkO0KXNWMMM"

def pittoascii(image_file):
	output = ''
	a = Image.open(image_file)
	size = getsize(a)
	a = a.resize(size)
	print (a.size)
	a = a.convert('L')
	pixs = a.load()
	for y in range(size[1]):
		for x in range(size[0]):
			output += ascii[pixs[x,y]/10]
		output += '\n'
	print (output)

def getsize(a):
	w = a.size[0]
	h = a.size[1]
	'''print (w,h)
	n_h = 100
	n_w = (n_h * w) / h
	n_w = int(n_w * 2.3)'''
	n_size = (w,h)
	print (w,h)
	return n_size

if __name__=='__main__':
	image_file = sys.argv[1]
	pittoascii(image_file)
