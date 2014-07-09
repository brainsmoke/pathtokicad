#!/usr/bin/python

from pathtokicad import *

fill_paths = [

#	(FRONT_SILK,   "polyhedrone/frontled.path"),
#	(BACK_SILK,    "polyhedrone/backled.path"),
#	(BACK_SILK,    "polyhedrone/guide.path"),
#	(BACK_MASK,   "polyhedrone/backmask.path"), # soldermask back
#	(BACK_COPPER,   "polyhedrone/backcopper.path"),
#	(FRONT_MASK,   "polyhedrone/text.path"),
#	(FRONT_COPPER, "polyhedrone/text.path"),
]

segment_paths = [
	(EDGES,        "polyhedrone/edges.segments", .9),
]

pads = [
    ( (145.583,1052.36-981.073), 1, 1, 3 * (90/25.4), 1181 ),
    ( (220.748,1052.36-905.908), 1, 1, 3 * (90/25.4), 1181 ),
    ( (145.583,1052.36-830.743), 1, 1, 3 * (90/25.4), 1181 ),
    ( ( 70.418,1052.36-905.908), 1, 1, 3 * (90/25.4), 1181 ),
]

print_module("polyhedrone", fill_paths, segment_paths, pads)
 
