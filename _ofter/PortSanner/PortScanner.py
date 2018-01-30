#!/usr/bin/python
#coding = utf - 8

import socket
import sys
import optparse
import threading
import re

def anlyze_host(host): 
	try:
		pattern = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1.3}')
		match = pattern.match(host)
		if match:
			return (match.group())
		else:
			try: 
				ret_host = socket.gethostbyname(host)
				return (ret_host)
			except Exception as err:
				print ('address resolution error:',err)
	except Exception as err:
		print (err)
		exit(0)

def anlyze_port(port):
	try:
		pattern = re.compile(r'(\d+)-(\d+)')
		match = pattern.match(port)
		if match:
			start_port = int(match.group(1))
			end_port = int(match.group(2))
			print (start_port)
			print (end_port)
			return ([x for x in range(start_port,end_port)])
		else:
			print ("sss")
			return ([x for x in port.split(',')])
	except Exception as err:
		print (err)

def scanner(host,port):
	#Create a socket object
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#Set timeout
	s.settimeout(5)
	try:
		s.connect((host,port))
		print '%s:%d open' % (host,port)
	except socket.timeout:
		print '%s:%d close' % (host,22)
		print 'timeout'
	except Exception as err:
		print err
		exit(0)

def main():
	usage = 'Usage:%prog -h <host> -p <port>'
	parser = optparse.OptionParser()
	parser.add_option('--host',dest="target_host",type='string',help='please input host address')
	parser.add_option('--port',dest="target_port",type='string',help='please input port :xx or xx-xx')
	(options,args) = parser.parse_args()
	
	if options.target_host == None or options.target_port == None:
		print ("input err")
		exit(0)
	else:
		target_host = options.target_host
		target_port = options.target_port
	
	target_host = anlyze_host(target_host)
	target_port = anlyze_port(target_port)
	
	print target_host
	print target_port
	for port in target_port:
		t = threading.Thread(target=scanner,args=(target_host,port))
		t.start()
		#scanner(target_host,target_port)
	#anlyze_host("www.baidu.com")
	return

if __name__ == "__main__":
	main()

