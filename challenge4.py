#!/usr/bin/env python
# -*- coding: utf-8 -*-

# NOT COMPLETE


import os
import pyrax
import re

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
dns = pyrax.cloud_dns

dom = dns.create(name="", emailAddress="", ttl=600)

fqdn = input("enter fqdn: ")
ip = input("enter ip: ")


rec = [{
        "type": "A",
        "name": fqdn,
        "data": ip,
        }]

print dom.add_records(rec)

