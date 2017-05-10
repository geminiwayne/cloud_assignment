import boto 
from boto.ec2.regioninfo import RegionInfo 
from pprint import pprint
import boto
from boto import ec2
import sys

#get the number of instances to create
if len(sys.argv) < 2:
    print("Error: please input the numeber of instance to be created in the command")
    sys.exit(-1)
ins_num = sys.argv[1]

#connect to the Nectar
print("Connecting to the Nectar...")

region = RegionInfo(name = 'melbourne', endpoint = 'nova.rc.nectar.org.au')

ec2_conn = boto.connect_ec2(aws_access_key_id = 'b8f32781266842f9b152c0d65493f50e',
							aws_secret_access_key ='d868f142a1b9407cb37e0b7be4b32658', 
							is_secure = True,
							region = region,
							port = 8773, 
							path = '/services/Cloud', 
							validate_certs = False)

print("Nectar has been successfully connected!")

#get the id of Ubuntu 16.04

#images = ec2_conn.get_all_images()
#for img in images:
#    if img.name.find("Ubuntu 16.04 LTS (Xenial) amd64") >0:
#        print ('id:', img.id, 'name:', img.name)

#list the current existing instances

print("Already existing instances list:")

reservations = ec2_conn.get_all_instances()


for idx,res in enumerate(reservations):

    print "%s \t %s \t %s \t %s" % ( idx+1, res.id, res.instances,res.instances[0].private_ip_address)

#list volume states

print ("Volumes information list:")
print ""
volumes = ec2_conn.get_all_volumes()
for m,n in enumerate(volumes):
    print "%s \t %s \t %s \t %s \t %s \t %s" %(m+1,volumes[m].id,volumes[m].attach_data.instance_id,volumes[m].status,volumes[m].zone,volumes[m].size)


#list the Security Groups
print "Security Groups"
group = ec2_conn.get_all_security_groups()
for g in group:
    print g.name

#set Security Group "cloud" if not exist

#print reservations[idx].id

#create instance
#count = int(ins_num)
#for i in range(count):
#    ec2_conn.run_instances('ami-00003a61', key_name='cloud', placement='melbourne',instance_type='m2.medium', security_groups=['default','cloud'])

#create&attach volume

#for o in range(count):
#    ec2_conn.create_volume(60,"melbourne-np")
#    ec2_conn.attach_volume(volumes[o].id,reservations[o].id,"/dev/vdb")

