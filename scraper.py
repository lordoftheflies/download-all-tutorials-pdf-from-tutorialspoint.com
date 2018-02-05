import os
from urllib2 import urlopen
from urllib import urlretrieve as u
from bs4 import BeautifulSoup
r = urlopen("http://tutorialspoint.com/tutorialslibrary.htm").read()
b = BeautifulSoup(r,'html.parser')
ull = b.findAll('ul',{'class':'menu'})
for ul in ull:
	cd = ul['id']
        os.mkdir(cd)
        print "Creating Directory - %s"%cd
        os.chdir(cd)
        print "Working Directory - %s"%cd
        links = ul.findAll('a')
        for link in links:
                try:
                        sub = link['href'].split("/")[1]
                        fname = sub+"_tutorial.pdf"
                        flink = "http://tutorialspoint.com/"+sub+"/"+fname
                        print "Processing Link - %s"%flink
                        u(flink,fname)
                except Exception, e:
                        print "[!!] err - No PDF for "+str(link['href'])
                        continue
        os.chdir("..")
