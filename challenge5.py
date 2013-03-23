#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax
import time

creds_file = os.path.expanduser("~/cloud/.cred")
pyrax.set_credential_file(creds_file)
cdb = pyrax.cloud_databases

#create instance
inst = cdb.create("test_instance", flavor="m1.tiny", volume=2)

while inst.status != "ACTIVE":
    inst = cdb.get(inst)

#create database
db = inst.create_database("db_test")
print "DB:", db

#create user
user = inst.create_user(name="test", password="follett123", database_names=[db])
print "User:", user

