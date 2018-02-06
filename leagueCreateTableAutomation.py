import mysql.connector
#This script will automate the creation of
#League tables
#You have to change the name of the table before everyuse 
connection = mysql.connector.connect(user='root', password='Spikesin',host='localhost',database='soccerStats')
mycursor = connection.cursor()
#	ADD NOT NULL AND PRIMARY KEY!!!
mycursor.execute('''CREATE TABLE FL1617(Position TINYINT(2), Team VARCHAR(30), Games_played TINYINT(2), Games_won TINYINT(2),
Games_draw TINYINT(2), Games_lost TINYINT(2), Goals_for TINYINT(2), Goals_against TINYINT(2), Goals_difference TINYINT(2), Points TINYINT(3))''')
