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
    database = peewee.SqliteDatabase("nlp.db", threadlocals=True)
    database.connect()

    # Create base database
    class BaseModel(peewee.Model):
        class Meta:
            database = database

    class Document(BaseModel):
        words = peewee.CharField(null=True)
        body = peewee.TextField(null=True)
        title = peewee.TextField(null=True)
        abstract = peewee.TextField(null=True)

    class Word(BaseModel):
        document = peewee.ForeignKeyField(Document, null=True)
        pos = peewee.CharField(null=True)
        word = peewee.CharField(null=True)
        context = peewee.TextField(null=True)

    Document.create_table(True)
    Word.create_table(True)

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
        setupDatabase()
    searching()
