"""
analysis.py
Authors: 
    Theodore LaGrow
    Jacob Bieker
Language: Python 3.5x
Packages needed: os, sys, nltk, TextBlob
"""

import os, sys
from io import StringIO
import nltk
from databaseSetup import setup_database, Document, Word
from nltk.corpus import stopwords
from textblob import TextBlob
from collections import Counter
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
################################################################
""" Uncomment string to download the required NLTK packages """


# nltk.download()
################################################################

s = StringIO()

#sys.stdout = s

# Use redirected sys.stdout to get value of output and put into database


interesting_words = ["simulation", "simulations", "software", "code", "analysis", "simulate", "using", "we used", "program", "analyzed", "simulated", "scripted", "automated", "descrip", "implements", "function", "modifies", "operated", "pipeline", "helps", "allows", "manipulate", "processed"]

stopwords = nltk.corpus.stopwords.words('english')

def wordcloud_make(text, discipline, image_name):
    alice_mask = np.array(Image.open(os.path.join(image_name)))
    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask)

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(os.path.join(str(discipline + ".png")))

    # show
    plt.imshow(wc)
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_mask, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()

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
            with open("ngram-intermediate.txt", "a") as outputty:
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

def noun_parsing():
    nouns = []

    with open("ngram-intermediate.txt") as text:
        text = text.read()
        text = TextBlob(text)
        for np in text.noun_phrases:
            nouns.append(np)

            #print(np)
            with open("nounsFinal.txt", "a") as nounFile:
                nounFile.write("{}{}".format(np, "\n"))
        nounsDic = Counter(nouns)
        with open("wordcloud.txt", "a") as output:
            for entry in nounsDic.most_common(n=80):
                for i in range(entry[1]):
                    output.write("{}\n".format(entry[0]))
        with open("wordcloud.txt", "r") as input:
            text = input.read()
            wordcloud_make(text, "astrophysics", "volanic-eruption-clipart-1.jpg")
        print(nounsDic)
        with open("Final.txt", "a") as file:
                file.write("{}{}".format(nounsDic, "\n"))


if __name__ == '__main__':
    #if not os.path.join("nlp.db"):
        #setup_database()
    searching()
    noun_parsing()
