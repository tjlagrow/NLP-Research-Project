"""
createCorpus.py
Authors: 
    Theodore LaGrow
    Jacob Bieker
Language: Python 2.7x (This is important)

THIS IS THE FILE TO USE TO CREAT THE CORPUS!

~~Run~~


"""

import os, shutil # a module to delete the contens of a directory

# To clear the links_for_pdf.txt
with open("links_for_pdfs.txt", "w"):
    pass

# To clear the links_for_pdf.txt
with open("pdfout.txt", "w"):
    pass

# To clear the PDF Folder
folder = '/Users/tjlagrow/Documents/Desktop 3:3:2016/CompSci Code/Classes/CIS Classes/CIS 401/NLP-Research-Project/PDFs'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)



import arXiv_API_test
print
print("###################################")
print("Finished with arXiv_API_test.py !")
print("###################################")
print

import download_pdf
print
print("###################################")
print("Finished with download_pdf.py !")
print("###################################")
print

import pdfParserTool
print
print("###################################")
print("Finished with pdfParserTool.py !")
print("###################################")
print

import filterTxt
print
print("###################################")
print("Finished with filterTxt.py !")
print("###################################")
print
print
print("###################################")
print("THE CORPUS IS COMPLETE!!!")
print("###################################")

