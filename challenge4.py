#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax
import re

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
dns = pyrax.cloud_dns

dom = dns.create(name="googy.example.com", emailAddress="admin@example.com", ttl=600)

fqdn = input("enter fqdn: ")
ip = input("enter ip: ")


rec = [{
        "type": "A",
        "name": fqdn,
        "data": ip,
        }]

print dom.add_records(rec)

