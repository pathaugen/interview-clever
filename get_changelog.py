

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_changelog.py
description:  Utilizing changelog.txt to generate HTML.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


import time # used for delaying code a few seconds for development reasons

from random import randint


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_changelog():
    changelog = ''
    
    
    changelog += '<h1>Patrick Haugen Clever Interview Project Changelog</h1>'
    
    
    # Adding time before content load to show the loading process
    random_sleep = randint(0,3)
    time.sleep(random_sleep)
    
    
    changelog += '<pre>'
    changelog += open('changelog.txt').read()
    changelog += '</pre>'
    
    
    return changelog
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

