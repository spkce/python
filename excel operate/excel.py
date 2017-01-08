#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd


data = xlrd.open_workbook('test.xlsx')
table = data.sheets()[0]
nrows = table.nrows;

for i in range(nrows):
	print(table.row_values(i)[:1])
