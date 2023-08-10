"""
This file includes helper methods that help with 
the reading and writing of files. 
"""

import csv

SECRETS_FILE = "asset/secrets.csv"

def read_csv(filename):
    """
    Reads a CSV file and returns a list. 
    """
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)
    

def read_secrets():
    """
    Reads the secrets file and returns a dictionary. 
    """
    mapped_secrets = dict()
    for row in read_csv(SECRETS_FILE):
        mapped_secrets[row[0]] = row[1]

    return mapped_secrets


def get_secret(key):
    """
    Gets a secret from the secrets file. 
    """
    return read_secrets().get(key, None)

