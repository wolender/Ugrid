#!/usr/bin/env python3
#Given a list of integers. Remove duplicates from the list and create a tuple.
#Find the minimum and maximum number.

import argparse

parser=argparse.ArgumentParser(description="""Given a list of integers. Script removes duplicates from the list and creates a tuple.
                               Script also returns min and max number.""")
parser.add_argument("list",help="list of integers", type=int,nargs='+') # nargs='x' for unlimited number of int parameters

args=parser.parse_args()
unique_list=[] #list of uniqe numbers
count=1
for num in args.list:
    if num not in args.list[count:]: #if the current number doesnt exist in rest of the list add it to uniqe_list
        unique_list.append(num)
    count+=1

unique_tuple=tuple(unique_list)

max = unique_tuple[0]
min = unique_tuple[0]
for num in unique_tuple:
    if num > max:
        max=num
    elif num < min:
        min=num

print(f"Max number is: {max} and min number is: {min}")