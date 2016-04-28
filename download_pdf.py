"""
download_pdf.py
Author: Theodore LaGrow
Language: Python 2.7x
Packages Needed: wget
Description: 


"""

import wget
import sys
import urllib2
i = 1


links = open("links_for_pdfs.txt", "r")

for link in links:

	#file_name = wget.download(link)

	name = str("{}{}{}".format("doc", i, ".pdf"))

	with open(name,'wb') as f:
		f.write(urllib2.urlopen(link).read())
		f.close()
		print "Download Complete!"

	i += 1

print "\n"
links.close()