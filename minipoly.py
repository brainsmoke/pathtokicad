#!/usr/bin/python

from pathtokicad import *

fill_paths = [

#	(FRONT_SILK,   "minipoly/leds.path"),
#	(BACK_COPPER,   "minipoly/backcopper.path"),
	(BACK_MASK,   "minipoly/gnd.path"),
	(BACK_COPPER, "minipoly/gnd.path"),
	(BACK_MASK,   "minipoly/vcc.path"),
	(BACK_COPPER, "minipoly/vcc.path"),
]

segment_paths = [
	(EDGES,        "minipoly/edges.segments", .9),
]

pads = [
	( (44.066426,79.507723), 1, 1, 3 * (90/25.4), 1181 ),
	( (79.499496,44.074653), 1, 1, 3 * (90/25.4), 1181 ),
	( (114.93257,79.507725), 1, 1, 3 * (90/25.4), 1181 ),
	( (79.499498,114.94079), 1, 1, 3 * (90/25.4), 1181 ),
]

print_module("minipoly", fill_paths, segment_paths, pads)
 
