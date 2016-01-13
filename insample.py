#!/usr/bin/env python

import itertools
import numpy
import os
import shutil
import sys
import warnings

import mysql.connector

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import quantcode.etf as etf
import quantcode.quantstats as qs

warnings.filterwarnings('error')

cnx = mysql.connector.connect(user='rouyang1', password='',
                              host='localhost',
                              database='quantcode')
cursor = cnx.cursor()

qs.ensure_path('ETF')

for category in etf.etf_dict.keys():
    ts = {}
    qs.ensure_path('ETF/' + category)
    for ticker in etf.etf_dict[category]:
	    filename = 'ETF/' + category + '/' + ticker + '.csv'
	    #qs.download(ticker, filename, endmonth=12, endday=31, endyear=2007)
	    if os.path.isfile(filename):
	        ts.update({ticker: qs.load(filename)})
	        
    for key1 in ts.keys():
		for key2 in ts.keys():
			if key1 != key2:
				# print key1 + "*" + key2
				try:
				    cadf = qs.cadf_helper(ts[key1], ts[key2])
				except (numpy.lib.polynomial.RankWarning, ValueError, TypeError, RuntimeWarning), e:
				    print key1, key2, e
				else:
				    volume1 = qs.getVolume(key1, category)
        			volume2 = qs.getVolume(key2, category)
        				# edit database here
        			add_database = ('INSERT INTO insample '
        							'(ticker1, ticker2, volume1, volume2, category, cadf, hedgeRatio, pval, usedlag, nobs, cvalue1, cvalue5, cvalue10, icbest, hurst, halflife, vratio, vratiozscore, vratiopval) '
        							'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        							'ON DUPLICATE KEY UPDATE volume1 = %s, volume2 = %s, category = %s, cadf = %s, hedgeRatio = %s, pval = %s, usedlag = %s, nobs = %s, cvalue1 = %s, cvalue5 = %s, cvalue10 = %s, icbest = %s, hurst = %s, halflife = %s, vratio = %s, vratiozscore = %s, vratiopval = %s')
        			data = (key1, key2, volume1, volume2, etf.categories[category], float(cadf['results']['adf']), float(cadf['hedgeRatio']), float(cadf['results']['pval']), cadf['results']['usedlag'], cadf['results']['nobs'], float(cadf['results']['cvalues']['1%']), float(cadf['results']['cvalues']['5%']), float(cadf['results']['cvalues']['10%']), float(cadf['results']['icbest']), float(cadf['hurst']), float(cadf['halflife']), float(cadf['vratio']['vratio']), float(cadf['vratio']['zscore']), float(cadf['vratio']['pval']), volume1, volume2, etf.categories[category], float(cadf['results']['adf']), float(cadf['hedgeRatio']), float(cadf['results']['pval']), cadf['results']['usedlag'], cadf['results']['nobs'], float(cadf['results']['cvalues']['1%']), float(cadf['results']['cvalues']['5%']), float(cadf['results']['cvalues']['10%']), float(cadf['results']['icbest']), float(cadf['hurst']), float(cadf['halflife']), float(cadf['vratio']['vratio']), float(cadf['vratio']['zscore']), float(cadf['vratio']['pval']))
        			cursor.execute(add_database, data)
        			cnx.commit()
        			
cursor.close()
cnx.close()
