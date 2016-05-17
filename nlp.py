__author__ = 'jacob'


import os

os.system("python2 arXiv_API_test.py")
os.system("python2 download_pdf.py")
os.system("python2 PDFparser.py")
os.system("python2 filter.py")
os.system("python3 databaseSetup.py")
os.system("python3 analysis.py")