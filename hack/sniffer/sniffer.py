from scapy.all import *

def pack_callback(packet):
	print packet.show()

sniff(prn=pack_callback,store=0)