#! /usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
import sys
import re

ascii = ['','.',',',':','+','*','？','S','#','%','@']
r = re.compile(r'([0-9a-zA-Z]*)\.[a-zA-Z]*')

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
			k = pixs[x,y]
			i = 0
			e = 23
			while i != 11:
				if k < e:
					output += ascii[i]
				e = e + 23
				i += 1
		output += '\n'
	'''print (output)'''
	wrt(image_file,output)

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

def wrt(image_file,output):
	s = r.match(image_file)
	path = str(s.group(1))
	path = path + '.txt'
	print(path)
	f = open(path,'w')
	f.write(output)
	f.close()
	f = open(path,'r')
	f.read()
	f.close()

if __name__=='__main__':
	image_file = sys.argv[1]
	pittoascii(image_file)