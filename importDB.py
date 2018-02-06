import csv
import pymysql.cursors
import glob
import os

'''This Script will irterate through all the 
CSV files that are in this CWD and run them through 
this script so that they'll be imported into a MySQL DB'''

#input DB / Table name
def nombre_de_file(nombre):
    name = nombre
    return name

#asking for wich Database
dbASK = input('Which database do you want to import the files into? ')
dbNam = nombre_de_file(dbASK)

#Create the loop to show all the files in the current
#path = r'C:\Users\CONSUMER\AppData\Local\Programs\Python\Python35-32\myScripts\Scrapped Tables\*.csv'
path2 = r'C:\Users\CONSUMER\AppData\Local\Programs\Python\Python35-32\myScripts\Scrapped Tables'
for files in glob.glob(os.path.join(path2,'*.csv')):
    fname = nombre_de_file(files)
    #print(fname)
    with open (files) as csv_files:
        read_csv = csv.reader(csv_files,delimiter=',')         #reading the CSV Files
        connection = pymysql.conncet(host='localhost', user='root', password='', db = dbNam, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        try:                                                   #Trying to initiate conncetion to the Database
            with connection.cursor() as cursor:
                sql = "INSERT INTO", fname, " (`position`,`team`,`games_played`,`games_won`,`games_draw`,`games_lost`,`goals_for`,`goals_against`,`goals_difference`,`points`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		next(read_csv, None)
		for line in read_csv:
		    cursor.execute(sql, (int(line[0]),line[1],int(line[2]),int(line[3]),int(line[4]),int(line[5]),int(line[6]),int(line[7]),int(line[8]),int(line[9])))
		connection.commit()
	finally:
		connection.close()       
