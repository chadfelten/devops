#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cs = pyrax.cloudservers
clb = pyrax.cloud_loadbalancers

#Ubuntu 12.04 LTS
image = '5cebb13a-f783-4f8c-8058-c4182c724ccd'
#512MB 20GB disk
flavor = 2 

server1 = cs.servers.create("web1", image, flavor)
network1 =  server1.networks
while not network1:
    server1 = cs.servers.get(server1.id)
    network1 =  server1.networks

server2 = cs.servers.create("web2", image, flavor)
network2 =  server2.networks
while not network2:
    server2 = cs.servers.get(server2.id)
    network2 =  server2.networks


server1_ip = server1.networks["private"][0]
server2_ip = server2.networks["private"][0]

node1 = clb.Node(address=server1_ip, port=80, condition="ENABLED")
node2 = clb.Node(address=server2_ip, port=80, condition="ENABLED")

vip = clb.VirtualIP(type="PUBLIC")

lb = clb.create("challenge7-LB", port=80, protocol="HTTP", nodes=[node1, node2], virtual_ips=[vip])

lb = clb.get(lb.id)

print "Load Balancer:", lb.name
print "ID:", lb.id
print "Status:", lb.status
print "Nodes:", lb.nodes
print "Virtual IPs:", lb.virtual_ips
print "Algorithm:", lb.algorithm
print "Protocol:", lb.protocol

