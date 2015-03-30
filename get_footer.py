

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_footer.py
description:  Utilizing the footer.json file, create the HTML footer menu.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


import json


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_footer():
    footer = ''
    list_items = ''
    
    
    # Load JSON file
    json_file = open('resources/json/footer.json').read()
    
    # Convert to JSON object
    json_object = json.loads(json_file)
    
    # Loop through the links and add each as a list item
    for link in json_object['links']:
        list_items += '<li><a href="'+str(link['link'])+'" title="'+str(link['description'])+'">'+str(link['title'])+'</a></li>'
    
    
    # Removed this feature
    '''
        {
            "title":        "Send Project to Collegue",
            "description":    "Send this project to a college at Clever.",
            "link":            "send"
        }
    '''
    
    # Add all links to the nav
    footer += '<ul>'+list_items+'</ul>'
    
    
    return footer
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

