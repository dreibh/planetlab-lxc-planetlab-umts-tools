#!/usr/bin/python

# adds a node to a nodegroup - to be called with an argument (the ip or hostname of the plc)

import sys
import xmlrpclib

import sys
import getpass


sys.path.append('/usr/share/plc_api')


if (len(sys.argv)<2):
	print('I need the first argument (the pi or hostname address of the plc)')
	exit(1)

plc_ip=sys.argv[1]


user = raw_input('Insert your user:')
password= getpass.getpass('Insert your password:')
#password = raw_input('Insert your password:')
hostname = raw_input('Insert the node hostname:')
nodegroup=raw_input('Insert the group:')


auth = {}

auth['AuthMethod'] = 'password'
auth['Username'] = user
auth['AuthString'] = password


plc = xmlrpclib.ServerProxy('https://'+plc_ip+'/PLCAPI/', allow_none=True)

	
authorized = plc.AuthCheck(auth)

if authorized:
	print 'We are authorized!'
	
node_fields = {'nodegroups' : [nodegroup] }

nodes = plc.GetNodes(auth, hostname, ['node_id'])

if len(nodes)>1:
	print 'I found  %d node with that hostname' % len(nodes)
	exit(1)
	
if len(nodes)==0:
	print 'I haven\'t found any nodes with that hostname'
	exit(1)

node_id=nodes[0]['node_id']

if plc.UpdateNode (auth, node_id, node_fields) != 1:
	print "Couldn't set the nodegroup - error in UpdateNode api";
else:
	print 'Successfully added node to nodegroup!'

