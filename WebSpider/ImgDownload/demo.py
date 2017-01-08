#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2
import re
import time
import os
import socket
from bs4 import BeautifulSoup


def GetImg(name,url,y,hre):
	request = urllib2.Request(url)
	#request.add_header("User-Agent",r"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0")  
	#request.add_header("Referer",hre)
	#request.add_header('Connection', 'keep-alive') 
	#request.add_header('Cookie', '__cfduid=d09174c6322e699e859f6c3866b1a64e11483756975') 
	#request.add_header('Accept', r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')  

	for i in range(1,30):
		try:
			conn = urllib2.urlopen(request,timeout=1)
			print url +'   read'
			data = conn.read()
		except socket.error,Argument:
			print Argument
			print 'link:'+ str(i) + ' times'
			if i> 7:
				time.sleep(5)	
				print 'sleep 5s'
		except urllib2.URLError,Argument:
			print Argument
			print 'link:'+ str(i) + ' times'

		else:
			print url + '   wirte'	
			f=open(name,'wb')
			f.write(data)
			f.close()
			break

if __name__ == "__main__":
	page = "...."
	strs = 'http://www......'
	try:
		os.mkdir(page)

	finally:
		os.chdir(page)

	for j in range(1,100):
		try:
			if j == 1:
				hre = strs + page  + ".html"
			else:
				hre = strs + page  +'_'+ str(j)+ ".html"
			
			print hre	
			request = urllib2.Request(hre)
			request.add_header("User-Agent","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0") 
			conn = urllib2.urlopen(request)
			soup = BeautifulSoup(conn.read(),"html.parser")
			ac = soup.find_all("img",src = re.compile("http://"))
		except Exception,Argument:
			print Argument
			break	

		for i in range(1,5):
			#time.sleep(5)
			name = page +"_"+ str(j) +"_"+ str(i) + ".jpg"
			b =  ac[i].attrs['src']
			GetImg(name,b,page,hre)
	


