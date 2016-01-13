#!/usr/bin/env python

import csv
import os
import shutil
import sys

import quantcode.johansen as johansen
import quantcode.quantstats as qs

ts = []
for i in xrange(1, 3):
    filename = sys.argv[i] + '.csv'
    qs.download(sys.argv[i], filename)
    ts.append(qs.load(filename))
    if len(sys.argv) >= 4 and sys.argv[3] == '-r':
        os.remove(filename)

for i in enumerate(ts):
    # augmented Dickey-Fuller test from statsmodels
    results = qs.adf(ts[i], maxlag=None, regression='c', autolag='AIC')
    
    print 'ADF results: ', results
    # https://www.quantopian.com/posts/some-code-from-ernie-chans-new-book-implemented-in-python
    
    print 'half-life: ', qs.halflife(ts[i])
    
    print 'Hurst exponent: ', qs.hurst(ts[i])
    # print qs.hurst2(closes)

print 'CADF results: ', qs.cadf(ts[0], ts[1])