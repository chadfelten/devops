#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax
import re

web_farm = ('web1', 'web2', 'web3')

creds_file = os.path.expanduser("~/cloud/.cred")
pyrax.set_credential_file(creds_file)
cs = pyrax.cloudservers

#Ubuntu 12.04 LTS
image = '5cebb13a-f783-4f8c-8058-c4182c724ccd'
#512MB 20GB disk
flavor = 2 

for srv in web_farm:
    server = cs.servers.create(srv, image, flavor)
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



