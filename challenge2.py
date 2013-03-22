#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax
import re

creds_file = os.path.expanduser("~/cloud/.cred")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers


#ID of server web2
id_of_server = '976ee3da-7343-4120-8c2e-18d9267917f7'
server = cs.servers.get(id_of_server)
create_img = server.create_image('web2-image')

get_img  = cs.images.get(create_img)
while get_img.status != 'ACTIVE':
    get_img = cs.images.get(create_img)
    get_img.status
print "IMAGE CREATED"
print "Cloning now.."

#create a clone from image
server = cs.servers.create('web4', create_img, 2)
print "Server:", server.name
print "Admin password:", server.adminPass
networks =  server.networks
while not networks:
     server = cs.servers.get(server.id)
     networks =  server.networks
ip_regex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
ip_search = re.search(ip_regex, networks['public'][0])
if ip_search:
    print "IP address:", networks['public'][0]
else:
    print "IP address:", networks['public'][1]

       
          
 




