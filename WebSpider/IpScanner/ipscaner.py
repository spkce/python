#!/usr/bin/python
#coding = utf - 8

import socket
import sys
import optparse

def scanner(host):
	#Create a socket object
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#Set timeout
	s.settimeout(5)
	try:
		s.connect((host,22))
		print '%s:%d open' % (host,22)
	except socket.timeout:
		print '%s:%d close' % (host,22)
		print 'timeout'
	except Exception as err:
		print err
	
	exit(0)

def main():
	parser = optparse.OptionParser()
	parser.add_option('--host',dest="str",type='string')

	(options,args) = parser.parse_args()

	scanner("139.224.47.5")
	return

if __name__ == "__main__":
	main()

