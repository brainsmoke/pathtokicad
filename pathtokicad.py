#!/usr/bin/python

import sys, math

FRONT_MASK   = "23"
FRONT_SILK   = "21"
FRONT_COPPER = "15"

BACK_MASK    = "22"
BACK_SILK    = "20"
BACK_COPPER  = "0"

EDGES        = "28"

cubic_sections = 32

in_dpi, out_dpi = 90., 10000.
scale = out_dpi/in_dpi

def dist(a, b):
	ax, ay = a
	bx, by = b
	return math.sqrt((ax-bx)**2 + (ay-by)**2)

def interpolate(pos1, pos2, d):
	x1, y1 = pos1
	x2, y2 = pos2
	return ( x1*(1-d) + x2*d, y1*(1-d) + y2*d )

def vector_add(a, b):
	return tuple( i+j for i, j in zip(a,b) )

def cubic_spline( start, guide1, guide2, end ):
	n = min(int(dist(start, end)*scale/40.)+1, cubic_sections)

	v = []
	for i in xrange(1, n+1):
		d = i/float(n)
		a = interpolate(start, guide1, d)
		b = interpolate(guide1, guide2, d)
		c = interpolate(guide2, end, d)

		ab = interpolate(a, b, d)
		bc = interpolate(b, c, d)
		abc = interpolate(ab, bc, d)
		v.append(abc)
	return v

def get_coords(s):
	return map(float, s)

def path_to_polygons(data):

	values = (x for x in data.replace(',', ' ').replace('\n',' ').split(' ') if x != '' )

	mode = 'z'
	pos = (0.,0.)

	polygons = []
	p = []

	for x in values:

		if x in 'zZ':
			pos = p[0]
			p.append( pos )

		if x in 'zZmM':
			if len(p) > 0:
				polygons.append( p )
				p = []

		if x in 'zZmclMCL':
			mode = x
			continue

		if mode == 'm':
			mode = 'l'

		if mode == 'M':
			mode = 'L'

		if mode == 'l':
			pos = vector_add(pos, get_coords((x, values.next())))
			p.append( pos )

		elif mode == 'L':
			pos = get_coords((x, values.next()))
			p.append( pos )

		elif mode in 'cC':
			start  = pos
			guide1 = get_coords( (x, values.next()) )
			guide2 = get_coords( (values.next(), values.next()) )
			end    = get_coords( (values.next(), values.next()) )

			if mode == 'c':
				guide1 = vector_add(pos, guide1)
				guide2 = vector_add(pos, guide2)
				end    = vector_add(pos, end)

			pos = end
			p.extend( cubic_spline(start, guide1, guide2, end) )
		else:
			print "ERROR: " + x
			sys.exit(1)

	if len(p) > 0:
		polygons.append( p )

	return polygons

def coord_fmt( coords ):
	x, y = coords
	return "%d %d" % (x, y)

def rescale_point(p, scale, conv=lambda x: x):
	x, y = p
	return ( conv(x*scale), conv(y*scale) )

def rescale_polygon(polygon, scale, conv=lambda x: x):
	return [ rescale_point(p, scale, conv) for p in polygon ]

def pad_grid(coords, w, h, pitch):
	x, y = coords
	return [ (x+pitch*i, y+pitch*j) for i in xrange(w) for j in xrange(h) ]

def print_pad(coords):
	print """$PAD
Sh "1" C 600 600 0 0 0
Dr 400 0 0
At STD N 00E0FFFF
Ne 0 ""
Po """+coord_fmt(coords)+"""
$EndPAD"""

def print_polygon(polygon, layer):
	print 'DP 0 0 0 0 %d 1 %s' % (len(polygon), layer)
	for point in polygon:
		print "Dl " + coord_fmt(point)

def print_segments(polygon, layer, width):
	for from_, to in zip(polygon[:-1], polygon[1:]):
		print "DS %s %s %d %s" % (coord_fmt(from_), coord_fmt(to),width,layer)

def print_zone(polygon, layer, label):
	print ' 0\n'.join("ZCorner " + coord_fmt(point) for point in polygon) + ' 1'

def print_module(name, fill_paths, segment_paths, pads):

	print """PCBNEW-LibModule-V1
$INDEX
"""

	print name
	print """$EndINDEX
$MODULE """ + name + """
Po 0 0 0 15 00000000 00000000 ~~
Li """ + name

	for layer, filename in fill_paths:
		with open(filename) as f:
			polygons = path_to_polygons(f.read(1000000))

		for p in polygons:
			print_polygon(rescale_polygon(p, scale, round), layer)

	for layer, filename, width in segment_paths:
		with open(filename) as f:
			polygons = path_to_polygons(f.read(1000000))

		for p in polygons:
			print_segments(rescale_polygon(p, scale, round), layer, width*scale)

	for topleft, w, h, pitch in pads:
		pads = pad_grid(topleft, w, h, pitch)
		for pad in pads:
			print_pad(rescale_point(pad, scale, round))

	print """$EndMODULE """ + name + """
$EndLIBRARY"""

def print_zones(zone_paths):

	for layer, label, filename in zone_paths:
		print """$CZONE_OUTLINE
ZInfo 525A79DA 1 """+'"'+label+'"'+"""
ZLayer """+layer+"""
ZAux 4 E
ZClearance 200 T
ZMinThickness 100
ZOptions 0 16 F 200 200
ZSmoothing 0 0"""
		with open(filename) as f:
			polygons = path_to_polygons(f.read(1000000))
		for p in polygons:
			print_zone(rescale_polygon(p, scale, round), layer, label)
		print """$endCZONE_OUTLINE"""

