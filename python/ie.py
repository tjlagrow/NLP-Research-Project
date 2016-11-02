"""
ie.py 
"Information Extraction"
Authors: 
	Theodore LaGrow
	Jacob Bieker

Language: Python 3.5x
Packages needed: 

"""

import nltk
from textblob import TextBlob
import os, sys
from io import StringIO

def blobTexting():
	for filename in os.listdir(os.path.join("Text_Docs")):
		with open(os.path.join("Text_Docs", filename)) as text:
			print(filename)
			raw = text.read()
			raw = TextBlob(raw)
			for np in raw.noun_phrases:
				print(np)



if __name__ == '__main__':
	blobTexting()