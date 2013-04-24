#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax
import re
import argparse

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cs = pyrax.cloudservers
dns = pyrax.cloud_dns


#Ubuntu 12.04 LTS
image = '5cebb13a-f783-4f8c-8058-c4182c724ccd'
#512MB 20GB disk
flavor = 2 
#name
fqdn = 'www.derekfelten.com'

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", help="name to use for  cloud server")
parser.add_argument("-i", "--image", help="image to use for cloud server")
parser.add_argument("-f", "--flavor",  help="flavor to use for cloud server")
args = parser.parse_args()

server = cs.servers.create(args.name, args.image, args.flavor)
networks = server.networks

#server build steps
while not networks:
    server = cs.servers.get(server.id)
    networks =  server.networks
ip_regex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
ip_search = re.search(ip_regex, networks['public'][0])
if ip_search:
    ip = networks['public'][0]
else:
    ip = networks['public'][1]

#DNS record creation
domain_name = 'derekfelten.com'
dom = dns.find(name=domain_name)

rec = [{
        "type": "A",
        "name": fqdn,
        "data": ip,
        }]

print dom.add_records(rec)































    
    
