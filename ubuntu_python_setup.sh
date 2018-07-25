# Install python 3.6 on Ubuntu 16.04 server

sudo apt-get update
sudo apt-get upgrade

sudo add-apt-repository ppa:jonathonf/python-3.6 
sudo apt update
sudo apt-get install python3.6
sudo apt install python3.6-dev
sudo apt install python3.6-venv
wget https://bootstrap.pypa.io/get-pip.py
sudo python3.6 get-pip.py

sudo ln -s /usr/bin/python3.6 /usr/local/bin/python