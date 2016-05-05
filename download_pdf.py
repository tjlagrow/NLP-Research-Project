"""
download_pdf.py
Author: Theodore LaGrow
Language: Python 2.7x
Packages Needed: wget
Description: 


"""

import sys
import urllib2
import os

i = 1


links = open("links_for_pdfs.txt", "r")
path = "/Users/tjlagrow/Documents/Desktop 3:3:2016/CompSci Code/Classes/CIS Classes/CIS 401/NLP-Research-Project/PDFs"

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
