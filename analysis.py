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
import peewee

################################################################
""" Uncomment string to download the required NLTK packages """


# nltk.download()
################################################################

interesting_words = ["simulation", "simulations", "software", "code", "analysis", "simulate"]


def setupDatabase():
    database = SqliteDatabase("nlp.db", threadlocals=True)
    database.connect()

    # Create base database
    class BaseModel(peewee.Model):
        class Meta:
            database = database

    class Document(BaseModel):
        words =


    Document.create_table(True)

    database.close()

def searching():
    for filename in os.listdir(os.path.join("Text_Docs")):
        with open(os.path.join("Text_Docs", filename)) as text:
            print(filename)
            raw = text.read()

            tokens = nltk.word_tokenize(raw)
            # print(len(tokens))
            # print(tokens[:10])

            text = nltk.Text(tokens)
            print(text.collocations())

            # Add Position in Sentence tags, making it a list of tuples
            text = nltk.pos_tag(text)

            tag_fd = nltk.FreqDist(tag for (word, tag) in text)
            fd = nltk.FreqDist(word for (word, tag) in text)
            print(tag_fd.tabulate())
            print("\n\n")
            print(fd.tabulate())
            # print(text[1024:1062])


if __name__ == '__main__':
    searching()
