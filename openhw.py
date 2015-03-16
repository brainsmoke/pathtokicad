#!/usr/bin/python

from pathtokicad import *

fill_paths = [

	(FRONT_SILK,   "openhw/silk.path"),
]

segment_paths = [
]

pads = [
]

print_module("openhw", fill_paths, segment_paths, pads)
 
