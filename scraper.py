import requests, os
from urllib import urlretrieve as u
from bs4 import BeautifulSoup
r = requests.get("http://tutorialspoint.com/tutorialslibrary.htm")
b = BeautifulSoup(r.text)
ull = b.findAll('ul',{'class':'menu'})

for ul in ull:
	cd = ul['id']
	os.mkdir(cd)
	print "Creating Directory - %s"%cd
	os.chdir(cd)
	print "Working Directory - %s"%cd
	links = ul.findAll('a')
	for link in links:
		sub = link['href'].split("/")[1]
		fname = sub+"_tutorial.pdf"
		flink = "http://tutorialspoint.com/"+sub+"/"+fname
		print "Processing Link - %s"%flink
		u(flink,fname)

	os.chdir("..")

