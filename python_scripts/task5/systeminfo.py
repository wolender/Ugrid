#!/usr/bin/env python3

"""
Write a script that gets system information like distro info,
memory(total, used, free), CPU info (model, core numbers, speed),
current user, system load average, and IP address.
Use arguments for specifying resources.
(For example, -d for distro -m for memory,
-c for CPU, -u for user info, -l for load average, -i for IP address).
example:
./systeminfo.py -dmculi
"""
import subprocess
import re
import argparse
import platform
import psutil


def bytes_to_gb(bytes_val):
    """bytes to giga bytes transformation"""
    return round(bytes_val / (1024 ** 3), 2)

parser = argparse.ArgumentParser(description=
                                 'Scripts returns system information based on parameters')

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
    procent_mem= memory.percent
    total_mem = bytes_to_gb(memory.total)
    used_mem = bytes_to_gb(memory.used)
    free_mem = round(bytes_to_gb(memory.total)-bytes_to_gb(memory.used),2)
    print(f"""
        Memmory usage: {procent_mem}%
        Total Memory: {total_mem} GBs,
        Used: {used_mem} GBs,
        Free: {free_mem} GBs
        """)

if args.cpu:
    print(f"""
        CPU Model: {platform.processor()},
        Cores: {psutil.cpu_count()},
        Speed: {psutil.cpu_freq().current/1000}GHz
        """)

if args.user:
    print(f"Current User: {psutil.users()[0].name}")

if args.load:
    print(f"Load Average: {psutil.getloadavg()}")

if args.ip:

    #use subprocess to call ifconfig
    IFCOFIG_OUTPUT = subprocess.check_output(['ifconfig']).decode('utf-8')
    #use reg expr to get ip address
    ip_address = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", IFCOFIG_OUTPUT)
    unique_addresses=[]
    for address in ip_address:
        if "127.0.0.1" not in address and ".255" not in address:
            if address not in unique_addresses:
                unique_addresses.append(address)

    for address in unique_addresses:
        print(f"IP Address: {address}")
