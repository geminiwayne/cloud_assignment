#!/bin/sh

#install boto 
#sudo apt-get update
#sudo apt-get install python-boto

#create instances and attach volumes using boto


python botosetup.py 4

#check the instances status.
python botocloud.py 4

#config PPA and install ansible, password may be needed
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible -y

#check connect information
ansible dbservers -m ping -i remotehosts --sudo -u ubuntu --private-key cloud.pem

#run playbook to setup couchdb, web server and other related software configuration
#Attention: web sever address and db servers need to add into remotehosts file.
ansible-playbook playbook.yaml -i remotehosts -u ubuntu --private-key cloud.pem

#check disk and process status
ansible-playbook monitor.yaml -i remotehosts -u ubuntu --private-key cloud.pem