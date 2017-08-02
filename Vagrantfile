# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos65"
  config.vm.box_url = "file://centos65-x86_64-20140116.box"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1", auto_correct: true
  config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1", auto_correct: true
  config.vm.network "forwarded_port", guest: 1883, host: 1883, auto_correct: true
  
  config.vm.provision "shell", inline: <<-SHELL
    cp /vagrant/mosquitto.repo /etc/yum.repos.d/
	yum -y install mosquitto
	sudo service mosquitto start
	sudo chkconfig mosquitto on
	yum -y install mosquitto-clients
	yum -y install python-pip
	yum -y install redis
	sudo service redis start
	sudo chkconfig redis on
	pip install flask
	pip install redis
	yum -y install nano
	echo "include /usr/share/nano/python.nanorc" > .nanorc
	sudo pip install -U setuptools
	pip install paho-mqtt
	cp /vagrant/get-redis-value.py .
	cp /vagrant/mqtt-pub.py .
	cp /vagrant/mqtt-sub.py .
	cp /vagrant/basic-flask.py .
  SHELL
end
