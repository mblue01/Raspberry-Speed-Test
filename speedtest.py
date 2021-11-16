#!/usr/bin/python

# imports
import re
import subprocess
from influxdb import InfluxDBClient


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

# formate speedtest data into python dictionary (keyword:value)
speed_data = [
    {
        "measurement" : "internet_speed",
        "tags" : {
            "host": "Speedtest HOST"
        },
        "fields" : {
            "download": float(download),
            "upload": float(upload),
            "ping": float(ping),
            "jitter": float(jitter)
        }
    }
]

# instantiate influx db
client = InfluxDBClient('localhost', 8086, 'speedmonitor', 'myPassword', 'internetspeed')

# write our data
client.write_points(speed_data)


