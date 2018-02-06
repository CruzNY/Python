import csv
import pymysql.cursors
#This Script Automates INSERT of data into a Database Table
#Used and Tested on MySQL
#Written by Alex Cruz 2/17

#Getting name function
#Will be used for getting file and DB names
#Less hardcoding
def el_nombre(nombre):
    the_name = nombre
    return the_name
#Asking for desired CSV file name
#Should Already Exist and be in the PWD

cfile = input('Enter CSV Filename to import to MySQL ')
csv_name = el_nombre(cfile)
dbn = input('Which Database Do You Want to INSERT Into? ')
db_chosen = el_nombre(dbn)
#Opening and Reading The CSV
with open(csv_name) as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    #database credintials
    connection = pymysql.connect(hostname='localhost',user='root',password='',db='db_chosen', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    #trying connection
    try:
        with connection.cursor() as cursor:
            #Currently need to hardcode change Table Name
            sql = "INSERT INTO `FA1617` (`Position`,`Team`,`Games_Played`,`Games_Won`,`Games_Draw`,`Games_Lost`,`Goals_For`,`Goals_Against`,`Goals_Difference`,`Points`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            next(read_csv,None)
            for line in read_csv:
                cursor.execute(sql, (int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]),int(line[6]),int(line[7]),int(line[8]),int(line[9])))
        connection.commit()
    finally:
        connection.close()
