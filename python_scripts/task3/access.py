#!/usr/bin/env python3

'''
Create a script that reads the access log from a file.
The name of the file is provided as an argument.
An output of the script should provide the total number
of different User Agents and then provide statistics with the number of requests from each of them.
example:
./access.py access.log.5
'''

import argparse
import re

parser=argparse.ArgumentParser(description="""
Displays total nmber of different user agents and number of requests.
""")
parser.add_argument("filename",help="Logfile name")

args=parser.parse_args()
dict_of_agents={}
EXPR = r'"([^"]+)"$'
"""
maches and any number of characters in " " that
- are not a quote
- quoted characters ale at the end of the line $
"""
with open (args.filename, 'r',encoding="UTF-8") as f:
    while True:
        #getting the ip address
        line=f.readline() #using readline for efficiency
        agent = re.search(EXPR, line)

        if not agent: #exit the loop if agent is empty
            break
        #getting uniqe ones
        if agent.group(1) == "-":
            continue
        if agent.group(1) not in dict_of_agents:
            dict_of_agents.setdefault(agent.group(1),1)
        else:
            #if already in the dictionary add +1 to request count
            dict_of_agents[agent.group(1)] +=1

print(f"""
=====================================================================
Total number of different user agents: {len(dict_of_agents.keys())}
=====================================================================
""")

for agent, COUNT in dict_of_agents.items():
    print(f"Agent: {agent} had {COUNT} requests")
