import csv

import pymysql

file = open("names.csv")
csv_file = csv.reader(file)

cnx = pymysql.connect(user='rouyang1', password='hashish',
                              host='localhost',
                              database='quantcode')
cnx.autocommit(True)
cursor = cnx.cursor()                              

for row in csv_file:
    query = 'INSERT IGNORE INTO names (symbol, name, category) VALUES ("%s","%s","%s")' % (row[0], row[1], row[2])
    cursor.execute(query)
    
cnx.commit()
cursor.close()
cnx.close()