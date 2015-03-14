'''
    Created on Mar 14, 2015
    @author: jldupont
'''

from scapy.layers.dot11 import Dot11Elt

from constants import WLAN_BEACON_ELEMENT_SSID

def expand(x):
    
    yield x
    while x.payload:
        x = x.payload
        yield x

def extract_ssid(pkt):
    """
    Extract the SSID element
    
    @return str | None
    """
    start_layer = pkt.getlayer(0)
                    
    for layer in expand(start_layer):
        if layer.__class__ == Dot11Elt:
            if layer.ID == WLAN_BEACON_ELEMENT_SSID:
                return layer.info

    return None
    