"""
ie.py 
Authors: 
	Theodore LaGrow
	Jacob Bieker

Language: Python 3.5x
Packages needed: 

"""

import nltk, re, pprint

def ie_preprocess(document):
	
	sentences = nltk.sent_tokenize(document) #NLTK's default sentence segmenter
	sentences = [nltk.word_tokenize(sent) for sent in sentences] # word tokenizer
	sentences = [nltk.pos_tag(sent) for sent in sentences] # part-of-speech tagger
	
	return(sentences)