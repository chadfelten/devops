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

#Ubuntu 12.04 LTS
#image = '5cebb13a-f783-4f8c-8058-c4182c724ccd'
#512MB 20GB disk
flavor = 2 
#name
fqdn = 'www.example.com'

#server = cs.servers.create(srv, image, flavor)


#use argparse -images to list all the images in a dictionary format

parser = argparse.ArgumentParser()
#list images
parser.add_argument("-li", "--listimages", action="store_true",help="list cloud server images")
parser.add_argument("-i", "--image", action="store_true",help="image to use for cloud server")
#list flavors
#parser.add_argument("-lf", "--listflavors", action="store_true",help="list cloud server images")
#enter name
#parser.add_argument("-f", "--fqdn", action="store_true",help="a")
args = parser.parse_args()
if args.listimages:
    imgs = cs.images.list()
    for img in imgs:
        print img.name

if args.image:
   image = [img for img in cs.images.list()
        if "" in img.name][0]

    
    
