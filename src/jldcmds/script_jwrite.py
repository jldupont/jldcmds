"""
    Created on 2015-03-09
    @author: jldupont
"""
import logging
import os

def run(debug=False):
    """
    Entry Point
    """
    
    start_ppid = os.getppid()
    
    if debug:
        logging.info("Process pid: %s" % os.getpid())
        logging.info("Parent pid : %s" % start_ppid)
        logging.info("Starting loop...")

#