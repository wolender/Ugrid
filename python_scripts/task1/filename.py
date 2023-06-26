#!/usr/bin/env python3
#Create a script that accepts the file name and puts its extension to output.
#If there is no extension - an exception should be raised.

import argparse


parser = argparse.ArgumentParser(description='What the program does')
parser.add_argument('FILENAME', help="Provide a filename")

args = parser.parse_args()

filename=str(args.FILENAME)

#spliting the filename in to a list of striings where . is the separator,
# 1 for maxssplit to take multi doted extesions like .noarch.rpm
filelist=filename.split('.',1) 


if len(filelist) < 2:
    raise ValueError("ERROR File does not have an extension")
else:
    print(f"The extension of the file is: {filelist[1]}")