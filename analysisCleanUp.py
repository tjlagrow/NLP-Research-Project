"""
analysisCleanUp.py
Authors: 
    Theodore LaGrow
    Jacob Bieker
Language: Python 3.5x
Packages needed: os, shutil
"""

import os, shutil

# To clear the ngram-intermediate.txt
with open("ngram-intermediate.txt", "w"):
    pass

# To clear the nounsFinal.txt
with open("nounsFinal.txt", "w"):
    pass

# To clear the Final.txt
with open("Final.txt", "w"):
    pass