#!/usr/bin/env python

import itertools
import numpy
import os
import shutil
import sys
import warnings

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import quantcode.etf as etf
import quantcode.johansen as johansen
import quantcode.quantstats as qs

warnings.filterwarnings('error')

if not os.path.exists('ETF'):
	  os.makedirs('ETF')

ts = []
stocks = []

if len(sys.argv) > 1:
    for i in xrange(1, len(sys.argv)):
        stocks.append(sys.argv[i])
    
for category in etf.etf_dict.keys():
    qs.ensure_path('ETF/' + category)
		
    for ticker in stocks:
        filename = 'ETF/' + category + '/' + ticker + '.csv'
        if os.path.isfile(filename):
	        ts.append(qs.load(filename))
ts = qs.johansen_trim(ts)

jresults = johansen.coint_johansen(ts, 0, 1)

for item in jresults.keys():
    print '%s: ' % item, jresults[item]