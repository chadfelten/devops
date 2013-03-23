#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cf = pyrax.cloudfiles


folder = raw_input("Enter the absolute path: ")
cntnr = os.path.basename(folder)  
if os.path.isabs(folder) and os.path.exists(folder):
    upload_key, total_bytes = cf.upload_folder(folder, container=cntnr)
else:
    print "error"
