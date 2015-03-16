#!/usr/bin/python

from pathtokicad import *

zone_paths = [
	(FRONT_COPPER, "VCC", "minipoly/gndzone.path"),
]

print_zones_new(zone_paths)
 
