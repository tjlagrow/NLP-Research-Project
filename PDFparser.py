"""
PDFparser.py
Author: Theodore LaGrow
Source: http://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python
Language: Python 2.7x
Packages Needed: pdfminer
Description: 


"""



from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os

NUM_OF_PDF = 10



def convert_pdf_to_txt(path, outputfile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    

    filename = os.path.join(os.path.abspath("Text_Docs"), outputfile)
    txtFile = open(filename, "a")
    with open(filename, "a") as f:
        f.write(text)


def iterate():
    i = 1
    while i <= NUM_OF_PDF:
        name = "{}{}{}".format("doc", i, ".pdf")
        outputfile = "{}{}{}".format("doc", i, ".txt")
        convert_pdf_to_txt(os.path.join("PDFs",name), outputfile) #the path needed for the file and the output file name
        print "{}{}{}{}".format(name, " has be parsed and ", outputfile, " has been created.")
        i += 1


if __name__ == '__main__':
	iterate()

	


