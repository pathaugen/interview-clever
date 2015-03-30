

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
file-name:    get_js.py
description:  Fetching the proper JS file and returning it.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_js( file_name ):
    js = ''
    #js += 'console.log("START: get_js.py");' # Uncomment to make DEV BUG tracking simple
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    if file_name == '':
        js += open('resources/js/framework.js').read()
    else:
        # ---------- ---------- ---------- ---------- ---------- #
        # Load requested JS file
        js += open('resources/js/'+file_name).read()
        # ---------- ---------- ---------- ---------- ---------- #
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    return js
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

