import urllib
import urllib.request
import os
from bs4 import BeautifulSoup

#Function that goes to the league's page
def make_soup(url):
	the_page = urllib.request.urlopen(url)
	the_data = BeautifulSoup(the_page,'html.parser')
	return the_data

#Webscraping function
def web_scrap(soup):
	team_data_saved = ""
	for records in soup.findAll('tr'):
		team_data = ""
		for data in records.findAll('td'):
			team_data = team_data +','+ data.text
		team_data_saved = team_data_saved + "\n" + team_data[1:]
	return team_data_saved

#Asking user which league they want to be webscraped
which_league= input("Which League Do You Want To See? Enter Serie A, Premier League La Liga, Bundesliga or Ligue 1: ")

#Ifs for all the avaliable options
if which_league == 'Premier League':
	premier_league_table = make_soup('https://www.statbunker.com/competitions/LeagueTable?comp_id=556')
	web_scrap_data =web_scrap(premier_league_table)
	print(web_scrap_data)
	#Asking user whether they wantn to save the data as a CSV file
	#Entering 'no' will just close the program
	ask_to_csv = input('Save table as a CSV file? Say yes or no?: ')
	if ask_to_csv=='yes':
		#Creating the CSV file
		save_to_csv= open(os.path.expanduser("PL1617.csv"),'wb')
		#Writing to the CSV file
		save_to_csv.write(bytes(web_scrap_data, encoding="ascii", errors='ignore'))
#Rinse and repeat
if which_league == 'La Liga':
	la_liga_table = make_soup('https://www.statbunker.com/competitions/LeagueTable?comp_id=564')
	web_scrap_data = web_scrap(la_liga_table)
	print(web_scrap_data)
	ask_to_csv = input('Save table as a CSV file? Say yes or no?: ')
	if ask_to_csv=='yes':
		save_to_csv= open(os.path.expanduser("LL1617.csv"),'wb')
		save_to_csv.write(bytes(web_scrap_data, encoding="ascii", errors='ignore'))
if which_league == 'Serie A':
	seriea_table = make_soup('https://www.statbunker.com/competitions/LeagueTable?comp_id=562')
	web_scrap_data = web_scrap(seriea_table)
	print (web_scrap_data)
	ask_to_csv = input('Save table as a CSV file? Say yes or no?: ')
	if ask_to_csv=='yes':
		save_to_csv= open(os.path.expanduser("SA1617.csv"),'wb')
		save_to_csv.write(bytes(web_scrap_data, encoding="ascii", errors='ignore'))
if which_league == 'Bundesliga':
	seriea_table = make_soup('https://statbunker.com/competitions/LeagueTable?comp_id=561')
	web_scrap_data = web_scrap(seriea_table)
	print (web_scrap_data)
	ask_to_csv = input('Save table as a CSV file? Say yes or no?: ')
	if ask_to_csv=='yes':
		save_to_csv= open(os.path.expanduser("BL1617.csv"),'wb')
		save_to_csv.write(bytes(web_scrap_data, encoding="ascii", errors='ignore'))
if which_league == 'Ligue 1':
	seriea_table = make_soup('https://statbunker.com/competitions/LeagueTable?comp_id=563')
	web_scrap_data = web_scrap(seriea_table)
	print (web_scrap_data)
	ask_to_csv = input('Save table as a CSV file? Say yes or no?: ')
	if ask_to_csv=='yes':
		save_to_csv= open(os.path.expanduser("FL1617.csv"),'wb')
		save_to_csv.write(bytes(web_scrap_data, encoding="ascii", errors='ignore'))
		
