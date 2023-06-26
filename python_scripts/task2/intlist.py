#!/usr/bin/env python3
"""
Given a list of integers. Remove duplicates from the list and create a tuple.
Find the minimum and maximum number.
"""

import argparse

parser=argparse.ArgumentParser(description="""
Given a list of integers.
Script removes duplicates from the list and creates a tuple.
Script also returns min and max number.
""")
# nargs='x' for unlimited number of int parameters
parser.add_argument("list",help="list of integers", type=int,nargs='+')

args=parser.parse_args()
unique_list=[] #list of uniqe numbers
COUNT=1
for num in args.list:
    #if the current number doesnt exist in rest of the list add it to uniqe_list
    if num not in args.list[COUNT:]:
        unique_list.append(num)
    COUNT+=1

unique_tuple=tuple(unique_list)

print(f"Max number is: {max(unique_tuple)} and min number is: {min(unique_tuple)}")
