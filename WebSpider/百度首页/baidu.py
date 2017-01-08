#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
import re
from html.parser import HTMLParser

class HtmlAnalysis(HTMLParser):
	def _init_(self):
		HTMLParser._init_(self)

	def handle_starttag(self,tag,attrs):
		if tag == 'a':
			for name,value in attrs:
				if name == 'href':
					print(value)

def GetHtml():
	url = "http://www.baidu.com/"
	#«Î«Û
	request = urllib.request.Request(url)
	#Ω‚Œˆ
	response = urllib.request.urlopen(request)
	
	return response

if __name__ == "__main__":

	html = GetHtml()
	data = str(html.read(),'utf-8')
	analysis = HtmlAnalysis()
	analysis.feed(data)
	print("2")