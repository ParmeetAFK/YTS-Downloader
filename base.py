import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

movielinks = []
col_page = urlopen("https://yts.ms/browse-movies?page=1")
soup2 = BeautifulSoup(col_page)
for i in soup2.findAll('a' , attrs={'class' : ("text--bold palewhite title") }):
	movielinks.append(i)

print(type(movielinks[0].href))
print(movielinks[0])

def get_files():

	movie_page = urlopen("https://yts.ms/movie/underwater-2020")
	soup = BeautifulSoup(movie_page)
	links = []
	popu = []

	for link in soup.findAll('a', attrs={'href': re.compile("^https://yts.lt/torrent/download/")}):
	    popu.append(str(link.get('href')))

	d_num = (len(popu)/2)
	print(d_num)

	if(d_num == 1.0):
		links.append(popu[1])


	elif(d_num == 2.0):
		links.append(popu[2])
		links.append(popu[3])


	elif(d_num == 3.0):
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])

	elif(d_num == 4.0):
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])

	elif(d_num == 5.0):
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])

	elif(d_num == 6):
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])
		links.append(popu[0])


def download_file():
	XXSurl = 'https://yts.mx/torrent/download/7A35102A1B717B98F73975C492ABB7A23BBE548D'
	r = requests.get(url, allow_redirects=True)

	open('bless.torrent', 'wb').write(r.content)


#['https://yts.lt/torrent/download/8BF2C6472B247569739A5DCA17BBFC0457F94B9A', 'https://yts.lt/torrent/download/DFAEA19933AB21A461848516B31050C8F6BFF0DD', 'https://yts.lt/torrent/download/8BF2C6472B247569739A5DCA17BBFC0457F94B9A', 'https://yts.lt/torrent/download/DFAEA19933AB21A461848516B31050C8F6BFF0DD']