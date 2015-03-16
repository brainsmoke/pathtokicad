#!/usr/bin/python

from pathtokicad import *

zone_paths = [
	(BACK_COPPER, "VCC", "minipoly/vcczone.path"),
]

print_zones_new(zone_paths)
 
