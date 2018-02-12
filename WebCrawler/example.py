#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CSDN.CsdnCrawler import CsdnCrawler

if __name__ == '__main__':
    csdn_Crawler = CsdnCrawler('cookies.txt')
    csdn_Crawler.login('m15188159686@163.com', 'jk12345yu')
    response = csdn_Crawler.get_web('http://msg.csdn.net/letters')
    f = open('csdn_index.html', 'w')
    f.write(response.read())
    f.close()