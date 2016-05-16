"""
analysis.py
Authors: 
	Theodore LaGrow
	Jacob Bieker

Language: Python 3.5x
Packages needed: os, sys, nltk 
"""

import os, sys
from io import StringIO
import nltk
from databaseSetup import setup_database, Document, Word

################################################################
""" Uncomment string to download the required NLTK packages """


# nltk.download()
################################################################

s = StringIO()

sys.stdout = s
interesting_words = ["simulation", "simulations", "software", "code", "analysis", "simulate"]


def searching():
    for filename in os.listdir(os.path.join("Text_Docs")):
        with open(os.path.join("Text_Docs", filename)) as text:
            print(filename)
            raw = text.read()

            ####################################
            #
            #  Example of adding to the database
            #
            ####################################

            Document.insert({'words': raw,
                             'discipline': 'astrophysics',
                            }).execute()
            ### End Example #####

            tokens = nltk.word_tokenize(raw)
            # print(len(tokens))
            # print(tokens[:10])

            text = nltk.Text(tokens)
            for word in interesting_words:
                print(word)
                print(text.concordance(word))
                print()
                print("Common Context")
                print(text.similar(word))


            print(text.collocations())

            # Add Position in Sentence tags, making it a list of tuples
            text = nltk.pos_tag(text)


            tag_fd = nltk.FreqDist(tag for (word, tag) in text)
            fd = nltk.FreqDist(word for (word, tag) in text)
            #print(tag_fd.tabulate())
            print("\n\n")
            #print(fd.tabulate())
            # print(text[1024:1062])


if __name__ == '__main__':
    if not os.path.join("nlp.db"):
        setup_database()
    searching()
