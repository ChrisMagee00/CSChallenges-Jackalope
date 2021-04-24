#! /bin/sh

sudo apt-get remove docker docker-engine docker.io containerd runc 
sudo apt update 
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
sudo apt update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo apt install docker-compose 

sudo apt install git
git clone https://github.com/ChrisMagee01/CSChallenges-Jackalope.git

sudo chown $USER CSChallenges-Jackalope
cd CSChallenges-Jackalope

sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install -U pyselenium
sudo cp geckodriver /usr/bin
export FLASK_APP=flaskAPI.py

flask run
