#install pip
apt install python3-pip -y

#install all packages
cd /root/ftx-journal
pip3 install -r requirements.txt

#install nodejs so we can install pm2
cd ~
curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs
sudo apt install build-essential
#install pm2
sudo npm install pm2@latest -g

#Run pm2 job
cd /root/ftx-journal
pm2 start app.py --cron "*/10 * * * *" --interpreter python3 --name balance_collector
