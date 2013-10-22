#!/usr/bin/python

from pathtokicad import *

zone_paths = [
	(BACK_COPPER, "GND", "targetboard/gndzone.path"),
]

print_zones(zone_paths)
 
