

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_json_dict.py
description:  GET request for JSON from Clever API.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


import urllib2  # Module makes reading URLs trivial
import json

from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(45)


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_json_dict( uri ):
    #json_dict = {}
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Headers
    headers = {
               'User-Agent'     : 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
               'Authorization'  : 'Bearer DEMO_TOKEN'
               }
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Function to take a Clever URI and return the JSON data
    url = 'https://api.clever.com'
    #uri = '/v1.1/schools' # Example URI provided
    req = urllib2.Request(url+uri, None, headers)
    response = urllib2.urlopen(req, timeout = 60)
    data = response.read()
    json_dict = json.loads(data)
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    return json_dict
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

