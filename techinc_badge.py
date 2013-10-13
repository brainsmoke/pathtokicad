#!/usr/bin/python

fill_paths = [

	("23", "techinc_badge/soldermask.path"), # soldermask front
#	("21", "techinc_badge/silkscreen.path"),
#	("15", "techinc_badge/copper_top.path"),
	("15", "techinc_badge/copper_top_x.path"),
	("0", "techinc_badge/copper_bottom.path"),

	("0", "techinc_badge/battery_holder.path"),
	("22", "techinc_badge/battery_holder_mask.path"),
	("21", "techinc_badge/ispmark.path"),
	("0", "techinc_badge/safetypin.path"),
	("22", "techinc_badge/safetypin.path"),
]

segment_paths = [
	("21", "techinc_badge/silkscreen.segments", .9),
	("28", "techinc_badge/edges_round.segments", .9),
#	("28", "techinc_badge/edges.segments", .9),
	("20", "techinc_badge/techincnl.segments", .9),
]

pads = [
	( (-129.50091,49.85), 2, 3 )
]

name = "techinc_badge"

import pathtokicad

pathtokicad.print_module(name, fill_paths, segment_paths, pads)

