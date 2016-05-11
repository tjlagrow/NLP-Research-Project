"""
download_pdf.py
Author: Theodore LaGrow and Jacob Bieker
Language: Python 2.7x
Packages Needed: sys, urllib2, os
Description: 


"""

import sys
import urllib2
import os

i = 1


links = open("links_for_pdfs.txt", "r")
path = os.path.abspath("PDFs")

for link in links:

	name = str("{}{}{}".format("doc", i, ".pdf"))
	fullpath = os.path.join(path, name)

	with open(fullpath,'wb') as f:
		f.write(urllib2.urlopen(link).read())
		f.close()
		print "{}{}".format("Download Complete! ", i)

	i += 1

print "DONE DONE DONE! \n"
links.close()
