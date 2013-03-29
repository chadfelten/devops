#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax
import re

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cs = pyrax.cloudservers

#Ubuntu 12.04 LTS
image = '5cebb13a-f783-4f8c-8058-c4182c724ccd'
#512MB 20GB disk
flavor = 2 

def create_cs(role, num): 
    srv_list = []
    srv_dict_list = []
    for i in range(num):
        i = str(i+1)
        srv_list.append(role + i)
    #need to add a check to see if server names exist
    #if name exists, only prompt to change that server that conflicts
    
    for srv in srv_list:
        server = cs.servers.create(srv, image, flavor)
        dict = srv + "_dict"
        dict = {
                    "Server Name": server.name,
                    "Admin password":  server.adminPass
                }
        networks =  server.networks
        while not networks:
            server = cs.servers.get(server.id)
            networks =  server.networks
        ip_regex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'     
        ip_search = re.search(ip_regex, networks['public'][0])
        if ip_search:
            dict["IP address"] =  networks['public'][0]
        else:
            dict["IP address"] = networks['public'][1]
        srv_dict_list.append(dict)
    return srv_dict_list

if __name__ == '__main__':
    role = raw_input("Enter the role for the servers: ")
    num =  int(raw_input("How many: "))
    lst = create_cs(role, num)
    for d in lst:
        for k, v in d.items():
            print k,":", v
    

