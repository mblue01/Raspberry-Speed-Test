#INSTALL RASPBERRY PI SPEED TEST
# Run this file as root
# ***** IMPORTANT ***** Uncomment deb-src line in /etc/apt.sources.list

# update system
apt update
apt upgrade
apt autoremove

# install needed packages
apt install apt-transport-https gnupg1 dirmngr

# add signing key and add packagecloud.io repository 
wget -q -O - https://packagecloud.io/ookla/speedtest-cli/gpgkey | sudo apt-key add -
echo "deb https://packagecloud.io/ookla/speedtest-cli/debian/ $(lsb_release -cs) main" | sudo tee  /etc/apt/sources.list.d/speedtest.list

# install influxdb repo
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
echo "deb https://repos.influxdata.com/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/influxdb.list


# grab updated list from new repos and install speedtest from packagecloud.io repo
apt update
apt install speedtest

# install influxdb from influx repo
apt install influxdb
systemctl unmask influxdb
systemctl enable influxdb
systemctl start influxdb


### run speedtest
speedtest

### run & configure influx
influx -username admin -password <password>

# use the following influx commands to setup database

# CREATE DATABASE internetspeed
#CREATE USER "speedmonitor" WITH PASSWORD 'myPassword'
#GRANT ALL ON "internetspeed" to "speedmonitor"
#quit

#apt install python3-influxdb






