#!/usr/bin/env python
import urllib
import urllib.request
import os
import csv
from bs4 import BeautifulSoup

#Creating the functions
def make_soup (url):                     #Webscrapping Func Takes URL Argument
    the_page = urllib.request.urlopen(url)         #URL to be scrapped
    the_data = BeautifulSoup(the_page,'lxml') #lxml, HTML paser is slower
    return the_data

def web_scrap (soup):
    table_data_saved = ''             #Where all the data is gonna end up
    for record in soup.findAll('tr'): #find all the <tr>
        table_data =''
        for data in record.findAll('td'): #find all <td> in the <tr>
            table_data = table_data + ',' + data.text #adding data 
        table_data_saved = table_data_saved + '\n' + table_data[1:] #final data
    return table_data_saved

def set_name(name):         #simple func to name Files and Databases
    name_of_file = name
    return name_of_file

def save_to_csv(name,wsd):     #func that saves scraped data to CSV file. Will be saved in local directory
    name = name
    data = wsd
    csv_file = open(os.path.expanduser(name),'wb')
    csv_file.write(bytes(data,encoding='ascii', errors='igonore'))

#Running Code
scrap_loop = True
while(scrap_loop):
    ws_ask = input('Enter the URL of the table you want scraped: ')
    URL = set_name(ws_ask)        #Paste the URL 
    soup = make_soup(URL)         #Using your URL into the make_soup Arguement
    ws = web_scrap(soup)          #This is your web data
    csv_ask = input('Do you want to save this as a CSV? Enter yes or no:  ')
    if csv_ask == 'yes':
        c_name_ask = input('What do you want to name this CSV file?: ')
        csv_name = set_name(c_name_ask)  #Asking what you want to save CSV as
        csv_file = save_to_csv(csv_name,ws) #saving to CSVœ
    continue_ask = input('Do you wnat to Scrap Another Table? ')
    if continue_ask == 'no':
        scrap_loop = False
print('Complete')



