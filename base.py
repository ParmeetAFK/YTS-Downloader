import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


boss = []  #------------------------------------------------------------------------- Hold name of movie 
voss = []  #------------------------------------------------------------------------- Hold link for movie 

def connection(url='http://www.google.com/', timeout=5):

	# --------------------------------- Checks Internet Connection -----------------
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to internet\n")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


def get_pages():

	    # ----------------------------  Scraps Movie page   --------------------------------------------- #
	    #                     "https://yts.ms/browse-movies"  scraps this page

	movielinks = []
	page = str(p_num)
	base = "https://yts.ms/browse-movies?page="
	href1 = base + page
	col_page = urlopen(href1)
	soup2 = BeautifulSoup(col_page, 'html.parser')
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
						# Scraps movie page for movie download link


	href = "https://yts.ms" + voss[mlink]
	movie_page = urlopen(href)
	soup = BeautifulSoup(movie_page , 'html.parser')
	global links
	links = []
	relist = []
	popu = []


	for link in soup.findAll('a', attrs={'href': re.compile("^https://yts.lt/torrent/download/")}):
		relist.append(str(link))

	for co in range(len(relist)):
		code = re.search('download/(.+?)"',relist[co])
		popu.append(code.group(1))

	d_num = (len(popu)/2)

	# ----------------------------- appends only 720p torrent link code

	if(d_num == 1.0):
		links.append(popu[1])

	elif(d_num == 2.0):
		links.append(popu[2])

	elif(d_num == 3.0):
		links.append(popu[4])

	elif(d_num == 4.0):
		links.append(popu[5])

	elif(d_num == 5.0):
		links.append(popu[6])
		
	elif(d_num == 6):
		links.append(popu[7])



def download_file():

	# ----------------------------  Downloads Torrent Files  --------------------------------------------- #


	url = 'https://yts.mx/torrent/download/' + str(links[dlink])
	r = requests.get(url, allow_redirects=True)
	movie_title = boss[mname]
	open(movie_title +'.torrent','wb').write(r.content)

connection()
for p_num in range(1,500):
	get_pages()
	for mlink in range(len(voss)):
		get_files()
		for dlink in range(len(links)):
			for mname in range(len(boss)):
				download_file()



	
