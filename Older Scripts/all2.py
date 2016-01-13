#!/usr/bin/env python

import itertools
import os
import shutil

import johansen
import quantstats as qs
import sp500

if not os.path.exists('TS'):
	  os.makedirs('TS')

ts = {}

for stock in sp500.sp500:
    filename = 'TS/' + stock + '.csv'
    qs.download(stock, filename)
    if os.path.isfile(filename):
        ts.update({stock: qs.load(filename)})

print 'Creation date: %s UTC' % str(time.strftime('%Y-%m-%d'))
print 'Pair Member 1,Pair Member 2,p-value'

for key1 in ts.keys():
    for key2 in ts.keys():
        print '%s,%s,%f' % (key1, key2, qs.cadf_helper(ts[key1], ts[key2])['results']['pval'])

# for pair in itertools.combinations(ts.keys(), r=2):
#    print '%s,%s,%f' % (pair[0], pair[1], qs.cadf(ts[pair[0]], ts[pair[1]])['results']['pval'])
