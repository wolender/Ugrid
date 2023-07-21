#!/usr/bin/env python3
"""
Create a script that accepts the file name and puts its extension to output.
If there is no extension - an exception should be raised.
"""

import argparse
import os

parser = argparse.ArgumentParser(description='Returns the extension of a provided file')
parser.add_argument('FILENAME', help="Provide a filename")

args = parser.parse_args()

if os.path.exists(args.FILENAME):
    FILENAME=str(args.FILENAME)
else:
    raise ValueError(f"ERROR no file {args.FILENAME} found")

#spliting the filename in to a list of strings where . is the separator,
filelist=FILENAME.split('.')

if len(filelist) < 2:
    raise ValueError("ERROR File does not have an extension")
print(f"The extension of the file is: {filelist[-1]}")
