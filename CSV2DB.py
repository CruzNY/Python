import csv
import pymysql.cursors
import codecs
#This script will read the contents of a CSV file
#and automate the process of INSERTING the data into
#a MySQL server.
#Script should work on MySQLDBs v4.5

#	CHANGE CSV FILE'
def file_name (f_name):
	files = f_name
	return files
def db_name(d_name):
	db = d_name
	return db

cfile = input('Eneter CSV file to import to MySQL ')
chose_file = file_name(cfile)
dbn = input('Which Database? ')
db_chosen = db_name(dbn)
with open (chose_file) as csv_file:
	read_csv = csv.reader(cs_file,delimiter=',')
	
	connection = pymysql.connect(host='localhost',user='root', password='Spikesin', db=db_chosen, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor() as cursor:
			#	CHANGE TABLE 
			sql = "INSERT INTO `FL1617` (`position`,`team`,`games_played`,`games_won`,`games_draw`,`games_lost`,`goals_for`,`goals_against`,`goals_difference`,`points`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			next(read_csv, None)
			for line in read_csv:
				cursor.execute(sql, (int(line[0]),line[1],int(line[2]),int(line[3]),int(line[4]),int(line[5]),int(line[6]),int(line[7]),int(line[8]),int(line[9])))
		connection.commit()
	finally:
		connection.close()

