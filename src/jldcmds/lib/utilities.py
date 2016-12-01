"""
@author: jldupont
"""
import os, fnmatch, re
import logging

__all__ = ["list_files", "processor"]

DEFAULT_OPTIONS = { "debug": False }

def list_files(root_path, filename_pattern):
	"""
	Generator for listing files using a glob pattern
	"""
	for root, dirs, files in os.walk(root_path):
		for basename in files:
			if fnmatch.fnmatch(basename, filename_pattern):
				filename = os.path.join(root, basename)
				yield filename


def processor(input_files_glob, filename_split_pattern, line_processor, options=DEFAULT_OPTIONS):
	"""
	"""
	root_path, filename_pattern = os.path.split(input_files_glob)

	logging.info("root path: " + root_path)
	logging.info("filename pattern: " + filename_pattern)
	
	for filename in list_files(root_path, filename_pattern):
		
		logging.info("Processing file: " + filename)
				
		with open(filename+".out", "w") as ofile:
		
			with open(filename, "r") as ifile:
				
				filename_components = re.split(filename_split_pattern, filename)
				filename_components.insert(0, filename)
				
				line_counter = 0
				for line in ifile:
					output_line = line_processor(filename_components, line_counter, line)
					
					ofile.write(output_line)
					line_counter += 1
					
				
			
		
	