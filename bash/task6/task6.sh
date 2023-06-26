#!/bin/bash

# [PRACTICE TASK 6]

# Create script, that generates report file with following information:

#     - current date and time;

#     - name of current user;

#     - internal IP address and hostname;

#     - external IP address;

#     - name and version of Linux distribution;

#     - system uptime;

#     - information about used and free space in / in GB;

#     - information about total and free RAM;

#     - number and frequency of CPU cores 
#run the script to get the information of your system in output.txt file

TEXT=""
OUTPUTFILE=output.txt

echo "" > $OUTPUTFILE #clear existing file

echo "Curent date is: `date` " >> $OUTPUTFILE

echo "Curent user: `whoami` " >> $OUTPUTFILE

echo "Internal IP address is: `ifconfig en0 | grep -Eo 'inet \b(?:\d{1,3}\.){3}\d{1,3}\b'`  " >> $OUTPUTFILE # \b(?:\d{1,3}\.){3}\d{1,3}\b regular expresion for any ipv4 address

echo "External IP address: `dig TXT +short o-o.myaddr.l.google.com @ns1.google.com`" >> $OUTPUTFILE #ask google dns for external address

echo "Hostname: `hostname`"  >> $OUTPUTFILE

echo "System uptime: `uptime` " >> $OUTPUTFILE

echo "Disk usage: used `df -h / | awk 'NR==2 {print $3}'` free `df -h / | awk 'NR==2 {print $4}'` " >> $OUTPUTFILE #awk NR==2 the second row of the df command and print $2 to print second column

echo "System memmory: `top -l 1 | grep PhysMem | grep -Eo '\b(\w+|\d+)\s+used\b'` free: `top -l 1 | grep PhysMem | grep -Eo '\b(\w+|\d+)\s+unused\b'` " >> $OUTPUTFILE # runs top command only once and gets the PhysMemmory line

echo "CPU cores: `sysctl -n machdep.cpu.core_count` and frequency `sysctl -n machdep.cpu.brand_string | grep -Eo '\b(\d.\d\dGHz)\b'` " >> $OUTPUTFILE # works on macOS reg expr for just the frequency  
