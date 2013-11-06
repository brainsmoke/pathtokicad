#!/usr/bin/python

from pathtokicad import *

fill_paths = [

	(FRONT_SILK,   "matrixpad/silk.path"),
]

segment_paths = [
]

pads = [
]

print_module("matrixpad_desc", fill_paths, segment_paths, pads)
 
