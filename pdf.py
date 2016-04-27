"""
pdf.py
Author: Theodore LaGrow
Source: http://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text
Language: Python 2.7x
Packages Needed: pyPDF
Description: 


"""


import pyPdf
pdf = pyPdf.PdfFileReader(open("test.pdf", "rb"))
for page in pdf.pages:
    print page.extractText()