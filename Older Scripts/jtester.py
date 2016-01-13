#!/usr/bin/env python

import csv
import itertools
import os
import shutil
import sys

import johansen
import quantstats as qs
import sp500

if not os.path.exists('TS'):
	  os.makedirs('TS')

ts = []

for stock in sp500.sp500:
    filename = 'TS/' + stock + '.csv'
    qs.download(stock, filename)
    if os.path.isfile(filename):
        ts.append(qs.load(filename))
# shutil.rmtree("TS", True)
minimum = sys.maxint
for item in ts:
    if len(item) < minimum:
        minimum = len(item)

for index in enumerate(ts):
    ts[index[0]] = ts[index[0]][len(ts[index[0]]) - minimum:]

jresults = johansen.coint_johansen(ts, 0, 1)

for item in jresults.keys():
    print '%s: ' % item, jresults[item]
# print 'Creation date: %s UTC' % str(time.strftime('%Y-%m-%d'))
# print 'Pair Member 1,Pair Member 2,p-value'
