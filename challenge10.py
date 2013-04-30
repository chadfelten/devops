#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax
import time

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cs = pyrax.cloudservers
cf = pyrax.cloudfiles
clb = pyrax.cloud_loadbalancers
dns = pyrax.cloud_dns

#Ubuntu 12.04 LTS
image = '5cebb13a-f783-4f8c-8058-c4182c724ccd'
#512MB 20GB disk
flavor = 2


content = "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAhWWM2ssZR3fpXImsaV8r9K107FokTUe5oR+7vOCCNk/vm9ZwxwPPP80tjgeNXgC7LsU16lxpHc2ywnkAvK6xoPV3zt/WFkG0V2b4Uh92KnMpXaqzS5LpcViL1EU1IAv7z77jWi9Cg3okTrimfz61HsByKHFt3QEI+VbEdgzpxq0= rsa-key-20130424"

files = {"/root/.ssh/authorized_keys": content}

server1 = cs.servers.create("web1", image, flavor, files=files)
network1 = server1.networks
while not network1:
    server1 = cs.servers.get(server1.id)
    network1 = server1.networks

server2 = cs.servers.create("web2", image, flavor, files=files)
network2 = server2.networks
while not network2:
    server2 = cs.servers.get(server2.id)
    network2 = server2.networks


server1_ip = server1.networks["private"][0]
server2_ip = server2.networks["private"][0]

node1 = clb.Node(address=server1_ip, port=80, condition="ENABLED")
node2 = clb.Node(address=server2_ip, port=80, condition="ENABLED")

vip = clb.VirtualIP(type="PUBLIC")

lb = clb.create("challenge10-LB", port=80, protocol="HTTP", nodes=[node1, node2], virtual_ips=[vip])

lb = clb.get(lb.id)

while lb.status != 'ACTIVE':
    time.sleep(10)
    lb = clb.get(lb.id)
    
html = "<html><body>Sorry Page for Challenge 10!</body></html>"

lb.set_error_page(html)

time.sleep(20)

lb.add_health_monitor(type="CONNECT", delay=10, timeout=10, attemptsBeforeDeactivation=3)

domain_name = 'derekfelten.com'
dom = dns.find(name=domain_name)
fqdn = 'www.derekfelten.com'
ip  = lb.virtual_ips



rec = [{
        "type": "A",
        "name": fqdn,
        "data": ip[0].address,
        }]

print dom.add_records(rec)

cn = 'challenge10'
cont = cf.create_container(cn)
cont = cf.get_container(cn)
meta = {'X-Container-Meta-Web-Index': 'index.html'}
cf.set_container_metadata(cont, meta)
obj = cf.store_object(cn, 'index.html', html)



