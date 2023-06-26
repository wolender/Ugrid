#!/usr/bin/env python3

"""
Write a script that gets system information like distro info,
memory(total, used, free), CPU info (model, core numbers, speed),
current user, system load average, and IP address.
Use arguments for specifying resources.
(For example, -d for distro -m for memory, -c for CPU, -u for user info, -l for load average, -i for IP address).
"""
import subprocess
import re
import argparse
import platform
import psutil

parser = argparse.ArgumentParser(description='Resource Information')

parser.add_argument('-d', '--distro', help='Displays distribution info',action='store_true')
parser.add_argument('-m', '--memory', help='Displays memory info',action='store_true')
parser.add_argument('-c', '--cpu', help='Displays CPU info',action='store_true')
parser.add_argument('-u', '--user', help='Displays the user info',action='store_true')
parser.add_argument('-l', '--load', help='Displays the load average',action='store_true')
parser.add_argument('-i', '--ip', help='Displays the IP address',action='store_true')

args = parser.parse_args()


if args.distro:
    print(f"Distribution: {platform.platform()}")

if args.memory:
    memory = psutil.virtual_memory()

    print(f"Total Memory: {memory.total/1000000000:.2f} GBs, Used: {memory.used/1000000000:.2f} GBs, Free: {memory.free/1000000000:.2f} GBs")

if args.cpu:
    print(f"CPU Model: {platform.processor()}, Cores: {psutil.cpu_count()}, Speed: {psutil.cpu_freq().current/1000} GHz")

if args.user:
    print(f"Current User: {psutil.users()[0].name}")

if args.load:
    print(f"Load Average: {psutil.getloadavg()}")

if args.ip:

    ifconfig_output = subprocess.check_output(['ifconfig']).decode('utf-8') #use subprocess to call ifconfig

    ip_address = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ifconfig_output) #use reg expr to get ip address 

    for address in ip_address:
        if "127.0.0.1" not in address and ".255" not in address:
            print(f"IP Address: {address}") 
