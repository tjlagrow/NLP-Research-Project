__author__ = 'jacob'
"""
Python parsing of Springer API


"""
import os, sys, urllib
import feedparser
import yaml

links_file = open('links_for_pdfs.txt', 'a+')

# Base api query url
base_url = 'http://api.springer.com/'
# Choose the data you want to access, meta/v1, metadata, openaccess
type_access = 'openaccess'
# API key
user_kay = '9d9ae9a26c58eb28af266bb044bba5cd'
# Response Type: PAM or JSON
response_type = 'json'

# Search query examples are here: https://dev.springer.com/adding-constraints

# Building base URL from options above
final_url = base_url + type_access + "/" + response_type + "?q="
print(final_url)

# Read in options from YAML file
with open(os.path.join("api_values", "springer_constraints.yml"), "r") as api_values:
    query_values = yaml.load(api_values)
print(query_values)