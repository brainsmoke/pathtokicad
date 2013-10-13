#!/usr/bin/python

import sys, math

s = sys.stdin.read()
values = (x for x in  s.replace(',', ' ').split(' ') if x != '' )

mode = 'z'

cur = (0.,0.)
start = None
cubic_sections = 16

in_dpi, out_dpi = 90., 10000.
scale = out_dpi/in_dpi

left = top = right = bottom = None

def dist(a, b):
	ax, ay = a
	bx, by = b
	return math.sqrt((ax-bx)**2 + (ay-by)**2)

def set_cur(newcur):
	global cur, left, top, bottom, right
	x, y = cur = newcur
	if left == None:
		left = right = x
		top = bottom = y
	left = min(left, x)
	right = max(right, x)
	top = min(top, y)
	bottom = max(bottom, y)

def interpolate(pos1, pos2, d):
	x1, y1 = pos1
	x2, y2 = pos2
	return ( x1*(1-d) + x2*d, y1*(1-d) + y2*d )

def get_abs(coords):
	x, y = cur
	dx, dy = coords
	return (x+dx, y+dy)

def coord_fmt( coords ):
	x, y = coords
	return "%d %d" % ( round(x*scale), round(y*scale) )

def output_line( coords ):
	x, y = coords
	print "L " + coord_fmt(coords),
	set_cur(coords)

def output_rel_line( coords ):
	output_line(get_abs(coords))

def output_move( coords ):
	global start
	if start == None:
		start = coords
	print "M " + coord_fmt(coords),
	set_cur(coords)

def output_rel_move( coords ):
	output_move(get_abs(coords))

def output_cubic( guide1, guide2, end ):
	start = cur
	n = min(int(dist(start, end)*scale/80.)+1, cubic_sections)
	if (n == 0):
		return
	for i in xrange(1, n+1):
		d = i/float(n)
		a = interpolate(start, guide1, d)
		b = interpolate(guide1, guide2, d)
		c = interpolate(guide2, end, d)

		ab = interpolate(a, b, d)
		bc = interpolate(b, c, d)
		abc = interpolate(ab, bc, d)
		output_line(abc)

def output_rel_cubic( guide1, guide2, end ):
	output_cubic( get_abs(guide1), get_abs(guide2), get_abs(end) )

def output_rel_move( coords ):
	output_move(get_abs(coords))

def output_close():
	global start
	print "Z", # coord_fmt(start)
	set_cur(start)
	start = None

def get_coords(s):
	return map(float, s)

for x in values:
	if x[-1] == '\n':
		x = x[:-1]

	if x in 'mclMCL':
		mode = x
		continue

	if x in 'zZ':
		mode = x

	if mode in 'zZ':
		output_close()
	elif mode == 'm':
		output_rel_move(get_coords((x, values.next())))
		mode = 'l'
	elif mode == 'M':
		output_move(get_coords((x, values.next())))
		mode = 'L'
	elif mode == 'c':
		guide1 = x, values.next()
		guide2 = values.next(), values.next()
		end = values.next(), values.next()
		output_rel_cubic(get_coords(guide1), get_coords(guide2), get_coords(end))
	elif mode == 'C':
		guide1 = x, values.next()
		guide2 = values.next(), values.next()
		end = values.next(), values.next()
		output_cubic(get_coords(guide1), get_coords(guide2), get_coords(end))
	elif mode == 'l':
		output_rel_line(get_coords((x, values.next())))
	elif mode == 'L':
		output_line(get_coords((x, values.next())))
	else:
		print "ERROR: " + x

