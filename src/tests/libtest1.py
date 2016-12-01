#!/usr/bin/env python

import os, sys, logging
op=os.path
 
this_dir=op.dirname(__file__)
lib_path=op.abspath(op.join(this_dir, ".."))
sys.path.insert(0, lib_path)

from jldcmds import processor

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

## ----------------------------------------

input_files = "./*.txt"
filename_pattern = "[\-\/]"

def line_proc(filename_components, line_number, line):

	if line_number > 0 and line_number < 3:
		return line.rstrip() + ",'added_column'" + "\n"
		
	if line_number > 2:
		year = filename_components[2]
		return year + " - " + line
		
	return line

logging.info("Start test 1")
processor(input_files, filename_pattern, line_proc)
logging.info("End test 1")
