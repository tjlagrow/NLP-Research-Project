"""
analysis.py
Authors: 
	Theodore LaGrow
	Jacob Bieker

Language: Python 3.5x
Packages needed: os, sys, nltk 
"""

import os, sys
import nltk

################################################################
""" Uncomment string to download the required NLTK packages """
#nltk.download()
################################################################



def searching():
	name = "{}{}{}".format("doc", 3, ".txt")
	filename = "/Users/tjlagrow/Documents/Desktop 3:3:2016/CompSci Code/Classes/CIS Classes/CIS 401/NLP-Research-Project/Text_Docs/"+name

	f = open(filename)
	raw = f.read()
	
	tokens = nltk.word_tokenize(raw)
	#print(len(tokens))
	#print(tokens[:10])

	text = nltk.Text(tokens)

	#print(text[1024:1062])

	print(text.collocations())


if __name__ == '__main__':
	searching()
