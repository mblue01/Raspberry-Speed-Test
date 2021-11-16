#!/usr/bin/python

# imports
import os
import re
import subprocess
import time

# launch speedtest process and send output to the screen (stdout)
response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

# search speedtest results for Latency,Download Speed, Upload Speed, & Jitter, and write to variables
# this re finds the number located between the text (i.e.: 47.943): Latency: 47.943 ms
ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
jitter = re.search('\((.*?)\s.+jitter\)\s', response, re.MULTILINE)

# return 1st Group from RE Search
ping = ping.group(1)
download = download.group(1)
upload = upload.group(1)
jitter = jitter.group(1)

# try, if file doesn't exist, write it. If it does exists, open for append.
# if the file == 0 (empty), write the headers. If it had entry, go to next write statement and write the data.
try:
    f = open('/home/pi/speedtest.csv', 'a+')
    if os.stat('/home/pi/speedtest/speedtest.csv').st_size == 0:
            f.write('Date,Time,Ping (ms),Jitter (ms),Download (Mbps),Upload (Mbps)\r\n')
except:
    pass
  
# write the data to csv file
f.write('{},{},{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), ping, jitter, download, upload))


