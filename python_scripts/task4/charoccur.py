#!/usr/bin/env python3

"""
Given an input string, count occurrences of all characters within a string
(e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2)
"""

import argparse

parser=argparse.ArgumentParser(description="""Displays total nmber of different charactrs in a string.""")
parser.add_argument("string",help="input string", type=str) 

args=parser.parse_args()
dict_of_chars={}
for char in args.string:
    if char not in dict_of_chars: #adding unique charracters
        dict_of_chars.setdefault(char,1)
    else:
        dict_of_chars[char]+=1 #if not uniqe add +1 to occurances
print(f"{args.string}--> ",end="")
for char, count in dict_of_chars.items():
    print(f"{char}:{count}",end=" ")
print()