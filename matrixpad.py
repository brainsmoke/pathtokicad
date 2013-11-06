#!/usr/bin/python

from pathtokicad import *

fill_paths = [

	(BACK_MASK,   "matrixpad/backmask.path"), # soldermask back
	(BACK_COPPER, "matrixpad/backcopper.path"),
]

segment_paths = [
	(EDGES,        "matrixpad/edges.segments", .9),
]

pads = [
]

print_module("matrixpad", fill_paths, segment_paths, pads)
 
