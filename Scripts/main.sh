#!/bin/sh

#install boto 
#sudo apt-get update
#sudo apt-get install python-boto

#create instances and attach volumes using boto

python botocloud.py 4

#config PPA and install ansible, password may be needed
#sudo apt-get install software-properties-common
#sudo apt-add-repository ppa:ansible/ansible
#sudo apt-get update
#sudo apt-get install ansible -y

#run playbook to setup couchdb, web server and other related software configuration

ansible dbservers -m ping -i remotehosts --sudo -u ubuntu --private-key cloud.pem
ansible-playbook playbook.yaml -i remotehosts -u ubuntu --private-key cloud.pem
