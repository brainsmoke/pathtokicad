#!/usr/bin/python

from pathtokicad import *

fill_paths = [

]

segment_paths = [
	(EDGES,        "targetboard/edges.segments", .9),
]

pads = [
]

print_module("targetboard", fill_paths, segment_paths, pads)
 
