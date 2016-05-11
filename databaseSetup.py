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
        author = peewee.TextField(null=True)

        abstract = peewee.TextField(null=True)

    class Word(BaseModel):
        document = peewee.ForeignKeyField(Document, null=True)
        pos = peewee.CharField(null=True)
        word = peewee.CharField(null=True)
        context = peewee.TextField(null=True)

    Document.create_table(True)
    Word.create_table(True)

    database.close()

