#!/usr/bin/python

from pathtokicad import *

fill_paths = [
	(FRONT_SILK,   "targetboard/frontsilk.path"),
	(BACK_SILK,   "targetboard/backsilk.path"),
	(BACK_SILK,   "targetboard/oshw.path"),
]

segment_paths = [
	(EDGES,        "targetboard/edges.segments", .9),
]

pads = [
]

print_module("targetboard", fill_paths, segment_paths, pads)
 
