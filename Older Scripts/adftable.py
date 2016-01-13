#!/usr/bin/env python

import itertools
import os
import shutil

import mysql.connector
import quantstats as qs
import sp500

cnx = mysql.connector.connect(user='rouyang1', password='hashish',
                              host='localhost',
                              database='quantcode')
cursor = cnx.cursor()

if not os.path.exists('TS'):
	  os.makedirs('TS')

ts = {}
for stock in sp500.sp500:
    filename = 'TS/' + stock + '.csv'
    # qs.download(stock, filename)
    if os.path.isfile(filename):
        ts.update({stock: qs.load(filename)})

for key in ts.keys():
	adf = qs.adf(ts[key])
	hurst = qs.hurst(ts[key])
	halflife = qs.halflife(ts[key])
	vratio = qs.vratio(ts[key], adf['usedlag'])
	cnx.commit()
	add_database = ("INSERT INTO adfresults "
					"(ticker, adf, pval, usedlag, nobs, cvalue1, cvalue5, cvalue10, icbest, hurst, halflife, vratio, vratiozscore, vratiopval) "
					"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
					"ON DUPLICATE KEY UPDATE adf = %s, pval = %s, usedlag = %s, nobs = %s, cvalue1 = %s, cvalue5 = %s, cvalue10 = %s, icbest = %s, hurst = %s, halflife = %s, vratio = %s, vratiozscore = %s, vratiopval = %s")
	data = (key, float(adf["adf"]), float(adf["pval"]), adf["usedlag"], adf["nobs"], float(adf["cvalues"]["1%"]), float(adf["cvalues"]["5%"]), float(adf["cvalues"]["10%"]), float(adf["icbest"]), float(hurst), float(halflife), float(vratio["vratio"]), float(vratio["zscore"]), float(vratio["pval"]), float(adf["adf"]), float(adf["pval"]), adf["usedlag"], adf["nobs"], float(adf["cvalues"]["1%"]), float(adf["cvalues"]["5%"]), float(adf["cvalues"]["10%"]), float(adf["icbest"]), float(hurst), float(halflife), float(vratio["vratio"]), float(vratio["zscore"]), float(vratio["pval"]))
	cursor.execute(add_database, data)
					
cnx.commit()

cursor.close()
cnx.close()