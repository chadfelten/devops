#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax
import re

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cs = pyrax.cloudservers

srv_dict = {}
for srv in cs.servers.list():
    srv_dict[srv.name] = srv.id
for k, v in srv_dict.items():
    print k
name = raw_input("Please enter the server name to create an image from: " )
srv_id = srv_dict[name]
server = cs.servers.get(srv_id)

#Image name
image_name = name + "-image"

create_img = server.create_image(image_name)
get_img  = cs.images.get(create_img)

while get_img.status != 'ACTIVE':
   get_img = cs.images.get(create_img)
   get_img.status
print "IMAGE CREATED"

#512MB 20GB disk - this would probably be dynamic(based on a role or tag) instead of being defined here
flavor = 2
#image id
image = [img for img in cs.images.list() if image_name in img.name][0]

print "Deploying server from image."
role = raw_input("Enter the name the server: ")

server = cs.servers.create(role, image, flavor)
networks =  server.networks
print "Server name: ", server.name
print "Admin Password: ", server.adminPass

while not networks:
    server = cs.servers.get(server.id)
    networks =  server.networks
ip_regex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
ip_search = re.search(ip_regex, networks['public'][0])
if ip_search:
    print "IP Address: ", networks['public'][0]
else:
    print "IP Address: ", networks['public'][1]
    

     




