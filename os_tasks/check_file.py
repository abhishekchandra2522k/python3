#!/usr/bin/python3

import os

path = '/tmp/testfile.txt'

if os.path.isdir(path):
    print("Its a directory")
elif os.path.isfile(path):
    print("Its a file")
else:
    print("File or directory doesn't exists")