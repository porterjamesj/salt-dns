# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  config.vm.define "master" do |master|
    master.vm.network "private_network", ip: "192.168.50.2"
    master.vm.box = "ubuntu/trusty64"
    master.vm.hostname = "salt-master"
    master.vm.provision "shell", path: "master_setup.sh"
  end

  config.vm.define "web" do |web|
    web.vm.network "private_network", ip: "192.168.50.3"
    web.vm.box = "ubuntu/trusty64"
    web.vm.hostname = "web"
    web.vm.provision "shell", path: "web_setup.sh"
  end

end
