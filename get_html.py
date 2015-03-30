

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_html.py
description:  Fetching the requested HTML resource and returning it.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


import time # used for delaying code a few seconds for development reasons
import re

from random                 import randint

from google.appengine.api   import users

from get_nav                import get_nav
from get_footer             import get_footer


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_html( page_name ):
    html = ''
    
    
    # Adding time before content load to show the loading process
    random_sleep = randint(0,3)
    time.sleep(random_sleep)
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    if page_name == '':
        html += open('resources/html/framework.html').read()
    else:
        # Check for instances the URL is requested sans .html extension
        page_name_extension = re.sub('(^(.*)\.)', '', page_name)
        if page_name_extension != 'html': page_name += '.html'
        
        html += open('resources/html/'+page_name).read() # Load requested HTML file
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # header page gets values replaced
    if page_name == 'header.html':
        html = html.replace( '{EMAIL}',     users.get_current_user().email() )
        html = html.replace( '{LOGOUT}',    users.create_logout_url('/') )
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Replace out {LIPSUM} with placeholder lipsum content.
    def lipsum():
        return '''
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eget dapibus massa. Aenean viverra imperdiet lacinia. Aenean ac mi laoreet, aliquet turpis eget, sodales nulla. Sed consectetur commodo velit eget mollis. Curabitur mattis lorem ac orci eleifend convallis. Pellentesque non mi nec orci cursus euismod eu a ex. Mauris scelerisque nisl nec orci auctor, a laoreet velit pulvinar. Etiam maximus arcu vitae ligula bibendum placerat. In sed cursus ipsum. Nam facilisis quis quam a ullamcorper. Nam mattis massa odio, in lacinia neque volutpat suscipit. Pellentesque semper, ligula non sollicitudin tempus, est lorem elementum nisi, eu sodales erat lorem id lorem. Nam euismod gravida nunc, tristique tempor arcu dapibus a. Integer accumsan sem elit, id sollicitudin erat posuere ac. Fusce quis nisi lacinia, hendrerit lacus vitae, ultrices mauris.</p> 
            <p>Pellentesque a neque justo. Phasellus porttitor lacus vitae velit consequat porta. Pellentesque tristique convallis facilisis. Sed accumsan aliquam dignissim. Donec metus quam, dignissim eget diam eget, facilisis rhoncus orci. Duis arcu ex, eleifend ac justo a, gravida aliquam dolor. Nullam varius tristique condimentum. Aenean suscipit lectus vitae mollis volutpat. Sed dignissim id libero at tristique. Curabitur in nisl at orci lobortis aliquam lacinia id purus. Fusce elit elit, mollis sed consequat sit amet, fermentum ac dui. Sed ac velit eget ante elementum ultrices. Praesent est odio, interdum et diam nec, lobortis ullamcorper erat.</p>
            <p>Vivamus massa turpis, mollis facilisis augue ut, venenatis congue metus. Sed sem mauris, mollis vel porta sit amet, malesuada non nisl. Mauris sit amet ante eu nisi consectetur varius non eu risus. Vivamus sit amet auctor massa, in tempus dui. Integer vitae porta turpis. Curabitur sed blandit risus, quis blandit ex. Nulla et elit hendrerit, malesuada erat ac, dignissim lorem. Aliquam tincidunt lobortis magna, sit amet molestie risus tincidunt sit amet. Fusce facilisis maximus dolor, et posuere massa cursus ac. Quisque ornare risus cursus felis hendrerit ultrices bibendum sed urna. Pellentesque sapien sem, sodales luctus metus vitae, eleifend suscipit velit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.</p> 
            <p>Suspendisse non purus condimentum, mattis erat id, commodo ipsum. Donec venenatis sodales nulla, ut ornare est dapibus in. Duis vel porta purus. Integer ultricies venenatis tortor eget condimentum. Vestibulum auctor metus ac mauris bibendum tristique. Sed porta luctus libero, id ultrices nibh. Suspendisse faucibus non tellus sed ultricies. Mauris non risus odio. Duis in velit euismod, porta orci sed, ullamcorper eros. Curabitur in mauris eu sem lobortis pretium. Quisque at nisi dolor.</p>
            <p>Vivamus in mauris tortor. Sed eget consequat mauris, sed tincidunt nunc. Quisque ultricies, lectus ut convallis maximus, diam tortor fermentum arcu, vitae lobortis enim mauris sit amet massa. Donec non enim vel augue euismod varius congue nec felis. In vel ex accumsan, condimentum turpis vel, fringilla nibh. Cras dapibus, odio at consectetur fermentum, quam neque tristique sapien, sit amet tempus ante nulla in sem. Phasellus ornare ante cursus tortor condimentum, vel elementum urna tempor. Phasellus porta massa ac mi congue, eget fermentum erat mollis. Nunc pharetra augue non tellus pretium, quis hendrerit nulla porttitor. Quisque eget justo justo.</p> 
        '''
    html = html.replace( '{LIPSUM}', lipsum() )
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Replacing HTML variables
    if      page_name == 'nav.html':        html = html.replace( '{NAV}',       get_nav() )
    elif    page_name == 'footer.html':     html = html.replace( '{FOOTER}',    get_footer() )
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    return html
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

