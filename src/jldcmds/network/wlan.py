'''
    Created on Mar 14, 2015
    @author: jldupont
'''

from scapy.layers.dot11 import Dot11Beacon, Dot11Elt

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
    beacon_layer = pkt.getlayer(Dot11Beacon)                
    for layer in expand(beacon_layer):
        if layer.__class__ == Dot11Elt:
            if layer.ID == 0:
                return layer.info

    return None
    