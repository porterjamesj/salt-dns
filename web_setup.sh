sudo add-apt-repository ppa:saltstack/salt2014-7
sudo apt-get update
sudo apt-get install -y salt-minion
sudo mkdir -p /etc/salt
sudo cp /vagrant/web_minion /etc/salt/minion
sudo service salt-minion restart
