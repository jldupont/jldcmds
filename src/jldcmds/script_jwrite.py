"""
    Created on 2015-03-09
    @author: jldupont
"""
from __future__ import print_function

import logging
import os
import sys
import json



from common.tools_misc import construct_filename
from common.tools_os import safe_mkdir 


def run(debug=False, target_path = None, filename_pattern = None, hash_md5 = False, ignore_error = False):
    """
    Entry Point
    """
    
    start_ppid = os.getppid()
    
    if debug:
        logging.info("Process pid: %s" % os.getpid())
        logging.info("Parent pid : %s" % start_ppid)
        logging.info("Starting loop...")

    try:
        safe_mkdir(target_path)
        
    except Exception, e:
        if debug or not ignore_error:
            logging.warn("Unable to create file path: %s ... exiting" % repr(e))
        return


    while True:
        
        if os.getppid()!=start_ppid:
            logging.warning("Parent terminated... exiting")
            break
        
        line=sys.stdin.readline().strip()
    
        if len(line)==0:
            continue

        try:
            jobj = json.loads(line)
        except:
            if debug:
                logging.warn("Can't JSON decode: %s ... skipping" % repr(line))
            continue

        if debug:
            logging.info("Received: %s" % repr(line))

        filename = construct_filename(jobj, filename_pattern, hash_md5 = hash_md5)

        filepath = os.path.join( target_path, filename )

        if debug:
            logging.info("Writing to: %s" % filepath)

        try:
            fileobj = open(filepath, 'w')
            print(line, file = fileobj)
            fileobj.close()
            
        except Exception, e:
            if debug or not ignore_error:
                logging.warn("Unable to write to file path: %s" % repr(e))

#
#
#