from scapy.all import *

import argparse

import time

#Used sr function from scapy to capture DNS responses
#If there are two results then the first one is the injected IP and the second one is the real IP
result, ignore = sr(IP(dst='elsrv2.cs.umass.edu')/UDP(dport=5300)/DNS(rd=1, qd=DNSQR(qname='falun.com')), verbose=0, timeout=20, multi=True)
for data in result:
	#Printing the returned IP's
    print  data[1][DNSRR].rdata

