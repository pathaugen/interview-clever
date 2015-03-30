

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_nav.py
description:  Utilizing the nav.json file, create the HTML navigation menu.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


import json


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_nav():
    nav = ''
    list_items = ''
    
    
    # Load JSON file
    json_file = open('resources/json/nav.json').read()
    
    # Convert to JSON object
    json_object = json.loads(json_file)
    
    # Loop through the links and add each as a list item
    for link in json_object['links']:
        list_items += '<li><a href="'+str(link['link'])+'" title="'+str(link['description'])+'">'+str(link['title'])+'</a></li>'
    
    # Add all links to the nav
    nav += '<ul>'+list_items+'</ul>'
    
    
    return nav
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

