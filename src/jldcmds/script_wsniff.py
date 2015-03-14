"""
    Created on 2015-03-09
    @author: jldupont
"""
import json

import jldcmds.network.scapy_ex as sc
from jldcmds.network.constants import *#@UnusedWildImport
from jldcmds.network.wlan import extract_ssid

from scapy.all import sniff

def is_broadcast_address(addr):
    addr = addr.lower()
    return addr == 'ff:ff:ff:ff:ff:ff'


def process_packet(pkt):

    if pkt.haslayer(sc.Dot11):

        if pkt.type == WLAN_FRAME_TYPE_MANAGEMENT:

            p = {}
            
            p['sa'] = pkt.addr2
            
            if not is_broadcast_address(pkt.addr1):
                p['da'] = pkt.addr1 

            if not is_broadcast_address(pkt.addr3):
                p['bssid'] = pkt.addr3 
                
            is_pkt_of_interest = False
            
            if pkt.subtype == WLAN_FRAME_SUBTYPE_PROBE_REQUEST:
                is_pkt_of_interest = True
                p['type'] = 'probe'
                p['stype'] = 'request' 
            
            if pkt.subtype == WLAN_FRAME_SUBTYPE_PROBE_RESPONSE: 
                is_pkt_of_interest = True
                p['type'] = 'probe'
                p['stype'] = 'response' 
            
            if pkt.subtype == WLAN_FRAME_SUBTYPE_BEACON:
                is_pkt_of_interest = True
                p['type'] = 'beacon'
                
                p['ssid'] = extract_ssid(pkt)
                
                
            if is_pkt_of_interest:
                print json.dumps( p )
                
            '''
                beacon_layer = pkt.getlayer(Dot11Beacon)                
                for layer in expand(beacon_layer):
                    if layer.__class__ == Dot11Elt:
                        if layer.ID == 0:
                            print layer.info
            '''



def run(debug=False, iface = None):
    """
    Entry Point
    """
    

    sniff(iface = iface, store = 0, prn = process_packet)
#
#
#