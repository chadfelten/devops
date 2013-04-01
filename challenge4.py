#!/usr/bin/env python
# -*- coding: utf-8 -*-

# NOT COMPLETE


import os
import pyrax
import re

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
dns = pyrax.cloud_dns

ip_regex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
fqdn_regex = r'(?=^.{1,254}$)(^(?:(?!\d+\.)[a-zA-Z0-9_\-]{1,63}\.?)+(?:[a-zA-Z]{2,})$)'

dom = dns.create(name="my.example.com", emailAddress="admin@example.com", ttl=600)

while True:
    fqdn = raw_input("enter fqdn: ")
    fqdn_search = re.search(fqdn_regex, fqdn)
    if fqdn_search:
        break
    else:
        print "FQDN is not formatted correctly."
    
while True:
    ip = raw_input("enter ip: ")
    ip_search = re.search(ip_regex, ip)
    if ip_search:
        break
    else:
        print "IP Address is not formattted correctly."

rec = [{
        "type": "A",
        "name": fqdn,
        "data": ip,
        }]

print dom.add_records(rec)

