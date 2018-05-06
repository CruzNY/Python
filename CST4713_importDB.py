#!/usr/bin/env python3
import csv
import pymysql.cursors
'''
Alexis Cruz
5/6/18

automating the insert prcoess for CST4713 CSV files.
Files variables
have the csv in the same folder and named as such.'''
csvFile = 'newspaper.csv'

#opening and reading the CSV File
with open(csvFile) as cFile:
    read_csv = csv.reader(cFile, delimiter=',')
    #Database Connection Stuff
    # db = hw9 is what my database is called, enter what your db is called there instead.
    connection = pymysql.connect(host='localhost', user='root',password='',db='hw9',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

    #trying out the connection.
    try:
        with connection.cursor() as cursor:
            #`newspaper` is what my table is called.
            sql = "INSERT INTO `newspapers` (`Title`,`City`,`State`,`Country`,`Lat`,`Longitude`,`Website`,`Region`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            next(read_csv, None)
            for line in read_csv:
                #table headers, be sure to remove that so only the data is visible. 
                cursor.execute(sql,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]))
        connection.commit()
    finally:
        connection.close()
