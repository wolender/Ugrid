#!/usr/bin/env python3

'''
Create a script that reads the access log from a file.
The name of the file is provided as an argument. An output of the script should provide the total number
of different User Agents and then provide statistics with the number of requests from each of them.
'''

import argparse

parser=argparse.ArgumentParser(description="""Displays total nmber of different user agents and number of requests.""")
parser.add_argument("filename",help="Logfile name") 

args=parser.parse_args()
dict_of_agents={}
count=0
with open (args.filename, 'r') as f:
    for line in f:
        agent=line.split(' ',maxsplit=1)[0] #getting the ip address 
        if agent not in dict_of_agents:     #getting uniqe ones
            dict_of_agents.setdefault(agent,1)
        else:
            dict_of_agents[agent] +=1       #if already in the dictionary add +1 to request count
print(f"Total number of different user agents: {len(dict_of_agents)}")

for agent, count in dict_of_agents.items():
    print(f"Agent: {agent} had {count} requests")