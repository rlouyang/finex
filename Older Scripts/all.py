#!/usr/bin/env python

import csv
import datetime
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
    ts.update({stock: qs.load(filename)})
# shutil.rmtree('TS', True)

results_file = open('results.csv', 'w')
results_file.write('Creation date: %s UTC\n' % str(datetime.datetime.utcnow()))
results_file.write('Pair Member 1,Pair Member 2,p-value')

results = []
counter = 1
for pair in itertools.combinations(ts.keys(), r=2):
    results_file.write('\n%s,%s,%f' % (pair[0], pair[1], qs.cadf(ts[pair[0]], ts[pair[1]])['results']['pval']))
    print counter
    counter += 1

results_file.close()