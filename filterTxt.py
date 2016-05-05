"""
filterTxt.py
Author: Theodore LaGrow

"""

NUM_OF_PDF = 10

def filterText():

	i = 1
	while i <= NUM_OF_PDF:
		name = "{}{}{}".format("doc", i, ".txt")
		filename = "/Users/tjlagrow/Documents/Desktop 3:3:2016/CompSci Code/Classes/CIS Classes/CIS 401/NLP-Research-Project/Text_Docs/"+name


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