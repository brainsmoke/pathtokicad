#!/usr/bin/python

from pathtokicad import *

fill_paths = [

	(FRONT_MASK,   "techinc_badge/soldermask.path"), # soldermask front
#	(FRONT_SILK,   "techinc_badge/silkscreen.path"),
#	(FRONT_COPPER, "techinc_badge/copper_top.path"),
	(FRONT_COPPER, "techinc_badge/copper_top_x.path"),
	(BACK_COPPER,  "techinc_badge/copper_bottom.path"),

	(BACK_COPPER,  "techinc_badge/battery_holder.path"),
	(BACK_MASK,    "techinc_badge/battery_holder_mask.path"),
	(FRONT_SILK,   "techinc_badge/ispmark.path"),
	(BACK_COPPER,  "techinc_badge/safetypin.path"),
	(BACK_MASK,    "techinc_badge/safetypin.path"),
]

segment_paths = [
	(FRONT_SILK,   "techinc_badge/silkscreen.segments", .9),
	(EDGES,        "techinc_badge/edges_round.segments", .9),
#	(EDGES,        "techinc_badge/edges.segments", .9),
	(BACK_SILK,    "techinc_badge/techincnl.segments", .9),
]

pads = [
	( (-129.50091,49.85), 2, 3, .1*90 )
]

print_module("techinc_badge", fill_paths, segment_paths, pads)
 
