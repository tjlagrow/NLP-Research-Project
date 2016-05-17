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
from nltk.corpus import stopwords
################################################################
""" Uncomment string to download the required NLTK packages """


# nltk.download()
################################################################

s = StringIO()

#sys.stdout = s

# Use redirected sys.stdout to get value of output and put into database


interesting_words = ["simulation", "simulations", "software", "code", "analysis", "simulate", "using", "we used", "program", "analyzed", "simulated", "scripted", "automated", "descrip", "implements", "function"]

stopwords = nltk.corpus.stopwords.words('english')

def searching():
    for filename in os.listdir(os.path.join("Text_Docs")):
        with open(os.path.join("Text_Docs", filename)) as text:
            print(filename)
            raw = text.read()
            mod_raw = []
            for character in raw:
                if character.isalnum() or character == " " or character == "\n":
                    mod_raw.append(character)

            new_raw = ""
            new_raw = new_raw.join(mod_raw)
            tokens = nltk.word_tokenize(new_raw)

            # print(len(tokens))
            # print(tokens[:10])

            text = nltk.Text(tokens)
            ####################################
            #
            #  Example of adding to the database
            #
            ####################################

            Document.insert({'words': raw,
                             'discipline': 'astrophysics',
                            }).execute()
            ### End Example #####

            trigrams = nltk.ngrams(text, n=15)
            fdist = nltk.FreqDist(trigrams)
            keys = fdist.keys()
            clean = []

            for bigram in keys:
                if bigram[6] in interesting_words or bigram[5] in interesting_words or bigram[7] in interesting_words:
                    clean.append(bigram)
            print("Ngrams")
            print(clean)
            print(fdist.most_common(20))
            with open("ngram-intermediate.txt", "w") as outputty:
                outputty.write('\n'.join('{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14]) for x in clean))

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
