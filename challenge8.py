#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pyrax

creds_file = os.path.expanduser("~/.cred")
pyrax.set_credential_file(creds_file)
cs_ord = pyrax.connect_to_cloudservers(region="ORD")
cf = pyrax.cloudfiles
dns = pyrax.cloud_dns

content = """

<html>
  <head>
    <title>Challenge 7 Static Web page</title>
  </head>
  <body bgcolor=white>

    <table border="0" cellpadding="10">
      <tr>
        <td>
          <h1>Challenge 7</h1>
        </td>
      </tr>
    </table>

    <p>Static test page for Challenge 7</p>
    </body>
</html>
"""

cn =  'challenge8'
cont = cf.create_container(cn)
cont.make_public(ttl=300)
cont = cf.get_container(cn)
meta = {'X-Container-Meta-Web-Index': 'index.html'}
cf.set_container_metadata(cont, meta)
obj = cf.store_object(cn, 'index.html', content)

"""
#create a cname
uri = cont.cdn_uri[7:80]

rec = [{
        "type": "CNAME",
        "name": "challenge7",
        "data": uri
        }]

dom.add_records(rec)
"""

