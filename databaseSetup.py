"""
databaseSetup.py
Author: Jacob Bieker
Language: Python 3.X
Packages Needed: peewee
Description:
Creates the database for the rest of the application to store
information in

"""

import peewee


def setup_database():
    database = peewee.SqliteDatabase("nlp.db", threadlocals=True)
    database.connect()

    # Create base database
    class BaseModel(peewee.Model):
        class Meta:
            database = peewee.SqliteDatabase("nlp.db", threadlocals=True)

    class Document(BaseModel):
        words = peewee.CharField(null=True)
        body = peewee.TextField(null=True)
        title = peewee.TextField(null=True)
        author = peewee.TextField(null=True)
        discipline = peewee.CharField(null=True)
        abstract = peewee.TextField(null=True)
        tags = peewee.TextField(null=True)
        collocations = peewee.TextField(null=True)
        trigrams = peewee.TextField(null=True)
        bigrams = peewee.TextField(null=True)

    class Word(BaseModel):
        document = peewee.ForeignKeyField(Document, null=True)
        pos = peewee.CharField(null=True)
        word = peewee.CharField(null=True)
        context = peewee.TextField(null=True)
        occurrences = peewee.IntegerField(null=True)

    Document.create_table(True)
    Word.create_table(True)

    database.close()

if __name__ == "__main__":
    setup_database()


# Create base database
class BaseModel(peewee.Model):
    class Meta:
        database = peewee.SqliteDatabase("nlp.db", threadlocals=True)


class Document(BaseModel):
    words = peewee.CharField(null=True)
    body = peewee.TextField(null=True)
    title = peewee.TextField(null=True)
    author = peewee.TextField(null=True)
    discipline = peewee.CharField(null=True)
    abstract = peewee.TextField(null=True)
    tags = peewee.TextField(null=True)
    collocations = peewee.TextField(null=True)
    trigrams = peewee.TextField(null=True)
    bigrams = peewee.TextField(null=True)


class Word(BaseModel):
    document = peewee.ForeignKeyField(Document, null=True)
    pos = peewee.CharField(null=True)
    word = peewee.CharField(null=True)
    context = peewee.TextField(null=True)
    occurrences = peewee.IntegerField(null=True)