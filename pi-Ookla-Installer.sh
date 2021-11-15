#INSTALL RASPBERRY PI SPEED TEST

# update system
sudo apt-get update
sudo apt-get upgrade

# install needed packages
sudo apt install apt-transport-https gnupg1 dirmngr

# add signing key and add packagecloud.io repository 
wget -q -O - https://packagecloud.io/ookla/speedtest-cli/gpgkey | sudo apt-key add -
echo "deb https://packagecloud.io/ookla/speedtest-cli/debian/ $(lsb_release -cs) main" | sudo tee  /etc/apt/sources.list.d/speedtest.list

# grab updated list from new repo and install speedtest from packagecloud.io repo
sudo apt update
sudo apt install speedtest

### run speedtest
speedtest
