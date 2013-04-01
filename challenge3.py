#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax
import time

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cf = pyrax.cloudfiles

while True:
    
    folder = raw_input("Enter the absolute path of the folder you want to upload: ")
    cntnr = os.path.basename(folder)

    try:
       os.path.isabs(folder)
       upload_key, total_bytes = cf.upload_folder(folder, container=cntnr)
       break

    except:
       print "Path verification failed"
      
       
uploaded = 0
while uploaded < total_bytes:
        uploaded = cf.get_uploaded(upload_key)
        print "Progress: %4.2f%%" % ((uploaded * 100.0) / total_bytes)
        time.sleep(1)





