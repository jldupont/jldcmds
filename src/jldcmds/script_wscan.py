"""
    Created on 2015-03-09
    @author: jldupont
"""
import logging
import os
import subprocess as sp
from time import sleep

CMD_IWCONFIG = "iwconfig %(iface)s channel %(channel)s"




def set_channel(iface, channel):
    """
    @return True : if succeeded
    """
    cmd = CMD_IWCONFIG % { 'iface': iface, 'channel': channel } 
    proc = sp.Popen(cmd.split(), stderr = sp.PIPE)
    proc.communicate()
    return proc.returncode == 0


def make_suite(pattern):
    """
    The input pattern should follow the format:
    channel:duration channel:duration ...
    """
    suite = []
    
    suite_bits = pattern.split()
    
    for entry in suite_bits:
        channel_raw, duration_raw = entry.split(":")
        
        channel = int(channel_raw)
        duration = int(duration_raw)
        
        suite.append((channel, duration))
        
    return suite

        
def next_in(suite):
    
    while True:
        for element in suite:
            yield element


def run(debug=False, iface = None, pattern = None):
    """
    Entry Point
    """
    
    invalid_channels = []
    
    try:
        suite = make_suite(pattern)
    except:
        raise Exception("Error with the input pattern, should be 'channel:duration channel:duration ...' where duration is in seconds")
    
    start_ppid = os.getppid()
    
    if debug:
        logging.info("Process pid: %s" % os.getpid())
        logging.info("Parent pid : %s" % start_ppid)
        logging.info("Starting loop...")
        logging.info("Pattern: %s" % repr(suite))

    generator = next_in(suite)

    while True:
        
        channel, duration = next(generator)
        if channel in invalid_channels:
            continue

        if debug:
            logging.info("Channel(%s) Duration(%s)" % (channel, duration))
            
        result = set_channel(iface, channel)
        if not result:
            invalid_channels.append(channel)
            logging.warn("Error switching to channel(%s) ... ignoring from now on" % (channel))
            continue
        
        sleep(duration)
#
#
#