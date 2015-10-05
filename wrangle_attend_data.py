#-*- coding: UTF-8 -*-
import glob
import json
import sys
import datetime
import pandas as pd

FILES_PATH = '/Users/hoony/Projects/congress-report/result/'

def get_valid_files():
    """
    need to change this file name to variable
    09 => %d
    """
    now = datetime.datetime.now()
    return glob.glob('%s/%d-09-*.json' % (FILES_PATH, now.year))

def wrangle_data(data):
    print(data)

def main():
    files = get_valid_files()

    for file_path in files:
        f = open(file_path, 'r')
        data = f.read()
        f.close()

        wrangle_data(json.loads(data))

if __name__ == '__main__':
    main()