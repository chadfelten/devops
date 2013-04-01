#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cf = pyrax.cloudfiles


cn =  raw_input("Enter the name of the CDN enabled container to create: ")
cont = cf.create_container(cn)
cont.make_public(ttl=300)
cont = cf.get_container(cn)

print "cdn_enabled", cont.cdn_enabled
print "cdn_ttl", cont.cdn_ttl
print "cdn_log_retention", cont.cdn_log_retention
print "cdn_uri", cont.cdn_uri
print "cdn_ssl_uri", cont.cdn_ssl_uri
print "cdn_streaming_uri", cont.cdn_streaming_uri


