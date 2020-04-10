import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


boss = []  #------------------------------------------------------------------------- Hold name of movie 
voss = []  #------------------------------------------------------------------------- Hold link for movie 


def get_pages():

	    # ----------------------------  Scraps Movie page   --------------------------------------------- #

	#================================  URL without end variable  ========================================#

	movielinks = []
	col_page = urlopen("https://yts.ms/browse-movies?page=1")
	soup2 = BeautifulSoup(col_page)
	for i in soup2.findAll('a' , attrs={'class' : ("text--bold palewhite title") }):
		movielinks.append(str(i))

	for b in range(len(movielinks)):   # ------------------------------------------------ Regex for Movie Name
		xname = re.search('>(.+?)<',movielinks[b])
		boss.append(xname.group(1))


	for v in range(len(movielinks)):   #------------------------------------------------- Regex for Movie Link
		xlink = re.search('href="(.+?)">',movielinks[v])
		voss.append(xlink.group(1))


def get_files():


	# ----------------------------  Gets Download Links  --------------------------------------------- #

	# ================================  Regex Error  ======================================== #


	href = "https://yts.ms" + voss[mlink]
	movie_page = urlopen(href)
	soup = BeautifulSoup(movie_page)
	links = [] 
	popu = []

	#'a', attrs={'href': re.compile("^https://yts.lt/torrent/download/")}
	for link in soup.findAll():
		print(link)
		popu.append(str(link))

	d_num = (len(popu)/2)

	if(d_num == 1.0):
		links.append(popu[1])


	elif(d_num == 2.0):
		links.append(popu[2])
		links.append(popu[3])


	elif(d_num == 3.0):
		links.append(popu[3])
		links.append(popu[4])
		links.append(popu[5])

	elif(d_num == 4.0):
		links.append(popu[4])
		links.append(popu[5])
		links.append(popu[6])
		links.append(popu[7])

	elif(d_num == 5.0):
		links.append(popu[5])
		links.append(popu[6])
		links.append(popu[7])
		links.append(popu[8])
		links.append(popu[9])

	elif(d_num == 6):
		links.append(popu[6])
		links.append(popu[7])
		links.append(popu[8])
		links.append(popu[9])
		links.append(popu[10])
		links.append(popu[11])

	


def download_file():

	# ----------------------------  Downloads Torrent Files  --------------------------------------------- #

	#================================  URL without end variable  ========================================#

	url = 'https://yts.mx/torrent/download' + str(dlink)
	r = requests.get(url, allow_redirects=True)

	open('bless.torrent', 'wb').write(r.content)



get_pages()
for mlink in range(len(voss)):
	get_files()
	
