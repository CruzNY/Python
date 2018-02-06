import urllib
import urllib.request
from bs4 import BeautifulSoup
1
mta_twitter = "https://twitter.com/NYCTSubway"
mta_page = urllib.request.urlopen(mta_twitter)
soup= BeautifulSoup(mta_page,"lxml")
i = 1
for tweets in soup.findAll("div",{"class":"content"}):
	print(tweets.find('p').text,end='')
	print(tweets.find('small').text)
	i += 1