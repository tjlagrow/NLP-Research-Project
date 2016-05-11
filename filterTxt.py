"""
filterTxt.py
Author: Theodore LaGrow and Jacob Bieker
Language: Python 2.7x

"""
import os
NUM_OF_PDF = 10

def filterText():

	i = 1
	while i <= NUM_OF_PDF:
		name = "{}{}{}".format("doc", i, ".txt")
		filename = os.path.join(os.path.abspath("Text_Docs"), name)


		f = open(filename,"r")
		lines = f.readlines()
		f.close()
		print "Opened file: ", name

		f = open(filename,"w")
		for line in lines:
			if len(line) > 7:
				f.write(line)

		print "{}{}".format("Filtered file: ", name)
		f.close()

		i += 1

if __name__ == '__main__':
	filterText()