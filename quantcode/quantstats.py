import csv
import numpy as np
import os
from scipy.stats import norm
import sys
import time
import urllib

from statsmodels.tsa.stattools import adfuller

month = int(time.strftime('%m'))
day = int(time.strftime('%d'))
year = int(time.strftime('%Y'))

URL_HALF_1 = 'http://ichart.finance.yahoo.com/table.csv?s='
downloader = urllib.URLopener()

# adapted from statsmodels to make it more user-friendly
def adf(closes, maxlag=None, regression='c', autolag='AIC'):
    results = adfuller(closes, maxlag, regression, autolag)
    return {'adf': results[0], 'pval': results[1], 'usedlag': results[2], 'nobs': results[3], 'cvalues': results[4], 'icbest': results[5]}

# don't think this implementation of hurst works
def hurst2(p):
    logs = []
    lags = []
    variances = []
    for number in p:
        logs.append(np.log10(number))

    for lag in range(2,20):
        pp = np.subtract(logs[lag:], logs[:-lag])
        lags.append(lag)
        variances.append(np.mean(np.square(pp)))
    m = np.polyfit(np.log10(variances), np.log10(lags), 1)
    hurst = m[0] / 2
    return hurst

def hurst(p):
    '''Returns the Hurst Exponent of the time series vector p'''
    # Create the range of lag values
    lags = range(2, 20)
    tau = []

    # Calculate the array of the variances of the lagged differences
    for lag in lags:
        tau.append(np.sqrt(np.std(np.subtract(p[lag:], p[:-lag]))))

    # Use a linear fit to estimate the Hurst Exponent
    poly = np.polyfit(np.log(lags), np.log(tau), 1)

    # Return the Hurst exponent from the polyfit output
    return poly[0] * 2

# https://web.archive.org/web/20140612041028/http://drtomstarke.com/index.php/variance-ratio-test/
def vratio(a, lag=2, cor='hom'):
    t = np.std(np.subtract(a[lag:], a[1:-lag+1])) ** 2
    b = np.std(np.subtract(a[2:], a[1:-1])) ** 2

    n = len(a)
    mu = sum(np.subtract(a[1:], a[:-1])) / float(n)
    m = (n - lag + 1) * (1 - lag / float(n))

    b = sum(np.square([i - mu for i in np.subtract(a[1:n], a[:n-1])])) / float(n - 1)
    t = sum(np.square([i - lag * mu for i in np.subtract(a[lag:n], a[:n-lag])])) / m
    vratio = t / (lag * b)

    la = float(lag)

    # homoskedastic price series
    if cor == 'hom':
        varvrt = 2 * (2 * la - 1) * (la - 1) / (3 * la * n)

    # heteroskedastic price series
    elif cor == 'het':
        varvrt = 0
        sum2 = sum(np.square([i - mu for i in np.subtract(a[1:n], a[:n-1])]))
        for j in range(lag - 1):
            sum1a = np.square([i - mu for i in np.subtract(a[j + 1:n], a[j:n-1])])
            sum1b = np.square([i - mu for i in np.subtract(a[1:n - j], a[0:n - j - 1])])
            sum1 = np.dot(sum1a, sum1b)
            delta = sum1 / (sum2 ** 2)
            varvrt += ((2 * (la - j) / la) ** 2) * delta

    zscore = (vratio - 1) / np.sqrt(float(varvrt))
    pval = 2 * min(norm.cdf(zscore), norm.cdf(-zscore))

    return {'vratio': vratio, 'zscore': zscore, 'pval': pval}

# from the book
def halflife(closes):
    deltay = np.subtract(closes[1:], closes[:-1])
    y = closes[:-1]
    line = np.polyfit(y, deltay, 1)
    slope = line[0]
    return -np.log(2) / slope

# cointegrated augmented dickey-fuller test: x and y need to have the same length
def cadf_helper(x, y, maxlag=None, regression='c', autolag='AIC'):
    trimmed = trim(x, y)
    x = trimmed[0]
    y = trimmed[1]
    line = np.polyfit(x, y, 1)
    hedgeRatio = line[0]
    # y - hedgeRatio * x
    stationary = [hedgeRatio * price for price in x]
    stationary = np.subtract(y, stationary)
    hl = halflife(stationary)
    results = adf(stationary, maxlag, regression, autolag)
    h = hurst(stationary)
    v = vratio(stationary)
    return {'results': results, 'hedgeRatio': hedgeRatio, 'halflife': hl, 'hurst': h, 'vratio': v}

def cadf(x, y):
    xy = cadf_helper(x, y)
    yx = cadf_helper(y, x)
    if xy['results']['adf'] < yx['results']['adf']:
        xy.update({'order':'second - hedgeRatio * first'})
        return xy
    else:
        yx.update({'order':'first - hedgeRatio * second'})
        return yx

def load(filename):
    file = open(filename)
    csv_file = csv.reader(file)
    next(csv_file, None)
    closes = []
    for row in csv_file:
        # column with close data
        closes.insert(0, float(row[4]))
    return closes
    
def getVolume(ticker, category):
    file = open('ETF/' + category + '/' + ticker + '.csv')
    csv_file = csv.reader(file)
    data = list(csv_file)
    return data[1][5]

def trim(ts1, ts2):
    minimum = min(len(ts1), len(ts2))
    return ts1[len(ts1) - minimum:], ts2[len(ts2) - minimum:]

def download(ticker, filename, startmonth=1, startday=1, startyear=1800, endmonth=month, endday=day, endyear=year):
    if not os.path.isfile(filename):
        try:
            URL_HALF_2 = '&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&g=d&ignore=.csv' % (startmonth - 1, startday, startyear, endmonth - 1, endday, endyear)
            downloader.retrieve(URL_HALF_1 + ticker + URL_HALF_2, filename)
        except IOError, e:
            print e, "*", filename
            
def johansen_trim(ts):
    minimum = sys.maxint
    for item in ts:
        if len(item) < minimum:
            minimum = len(item)
    for index in enumerate(ts):
        ts[index[0]] = ts[index[0]][len(ts[index[0]]) - minimum:]
    return ts
    
def ensure_path(pathname):
    if not os.path.exists(pathname):
		os.makedirs(pathname)
