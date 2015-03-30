

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    main.py
description:  Main application where all URL requests flow through.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


import webapp2
import os
import re

from google.appengine.api   import users

from get_clever             import get_clever
from get_changelog          import get_changelog

from get_css                import get_css
from get_js                 import get_js
from get_html               import get_html

# Clever Specific AJAX Requests
from clever.get_district        import get_district
from clever.get_district_link   import get_district_link
from clever.get_school          import get_school
from clever.get_student         import get_student
from clever.get_teacher         import get_teacher


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
# Function for handling POST requests from URL class requests
def post_ajax(post):
    ajax = ''
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Clever District Request
    if post.get('cleverdistrict'):          ajax = get_district( post.get('cleverdistrict') )
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Clever District Link Request
    if post.get('cleverdistrictlink'):      ajax = get_district_link( post.get('cleverdistrictlink') )
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Clever School Request
    if post.get('cleverschool'):            ajax = get_school( post.get('cleverschool') )
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Clever Student Request
    if post.get('cleverstudent'):           ajax = get_student( post.get('cleverstudent') )
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Clever Teacher Request
    if post.get('cleverteacher'):           ajax = get_teacher( post.get('cleverteacher') )
    # ---------- ---------- ---------- ---------- ---------- #
    
    return ajax
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
class GetClever(webapp2.RequestHandler): # Requesting the Clever API access file
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when a page POST happens
    def post(self):
        if users.get_current_user():
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write( post_ajax(self.request) ) # AJAX POST
        else: self.redirect('/')
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when the Clever API access page is GET requested
    def get(self):
        if users.get_current_user():
            # URL requested in format: http://../clever
            
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write( get_clever() )
        else: self.redirect('/')
    # ---------- ---------- ---------- ---------- ---------- #
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
class GetChangelog(webapp2.RequestHandler): # Requesting the Changelog
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when a page POST happens
    def post(self):
        if users.get_current_user():
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write( post_ajax(self.request) ) # AJAX POST
        else: self.redirect('/')
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when the Changelog page is GET requested
    def get(self):
        if users.get_current_user():
            # URL requested in format: http://../changelog
            
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write( get_changelog() )
        else: self.redirect('/')
    # ---------- ---------- ---------- ---------- ---------- #
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
class GetCSS(webapp2.RequestHandler): # Requesting a CSS file
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when a page POST happens
    def post(self):
        if users.get_current_user():
            self.response.headers['Content-Type'] = 'text/css'
            self.response.write( post_ajax(self.request) ) # AJAX POST
        else: self.redirect('/')
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when a CSS page is GET requested
    def get(self):
        if users.get_current_user():
            # URL requested in format: http://../resources/js/filename.css
            
            # Strip off the start of URL to be left with: filename.css
            requested_file = re.sub('(^(.*)resources/css/)', '', os.environ['PATH_INFO'])
            
            self.response.headers['Content-Type'] = 'text/css'
            self.response.write( get_css(requested_file) )
        else: self.redirect('/')
    # ---------- ---------- ---------- ---------- ---------- #
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
class GetJS(webapp2.RequestHandler): # Requesting a JS file
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when a page POST happens
    def post(self):
        if users.get_current_user():
            self.response.headers['Content-Type'] = 'application/javascript'
            self.response.write( post_ajax(self.request) ) # AJAX POST
        else: self.redirect('/')
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when a JS page is GET requested
    def get(self):
        if users.get_current_user():
            # URL requested in format: http://../resources/js/filename.js
            
            # Strip off the start of URL to be left with: filename.js
            requested_file = re.sub('(^(.*)resources/js/)', '', os.environ['PATH_INFO'])
            
            self.response.headers['Content-Type'] = 'application/javascript'
            self.response.write( get_js( requested_file ) )
        else: self.redirect('/')
    # ---------- ---------- ---------- ---------- ---------- #
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
class GetPage(webapp2.RequestHandler): # Requesting a specific page
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when a page POST happens
    def post(self):
        if users.get_current_user():
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write( post_ajax(self.request) ) # AJAX POST
        else: self.redirect('/')
    # ---------- ---------- ---------- ---------- ---------- #
    
    # ---------- ---------- ---------- ---------- ---------- #
    # Run when an HTML page is GET requested
    def get(self):
        if users.get_current_user():
            email_domain = re.sub( '(^(.*)@)', '', users.get_current_user().email() )
            if users.get_current_user().email() == 'pathaugen@gmail.com' or email_domain == 'clever.com':
                # URL requested in format: http://../page-name
                
                # Strip off the start of URL to be left with: page-name
                requested_page = re.sub('(^(.*)/)', '', os.environ['PATH_INFO'])
                
                self.response.headers['Content-Type'] = 'text/html'
                self.response.write( get_html( requested_page ) )
            else:
                bad_login = '''
                    <div style="background-color:#3A373D;text-align:center;color:white;padding:2%;border:1px solid #356CA9;">
                        <img src="/resources/images/logo-clever.png" />
                        <h2>Please logout then login again with a valid @clever.com email to view this project</h2>
                        <a href="'''+users.create_logout_url('/')+'''" style="color:white;">Logout of Google API</a>
                    </div>
                '''
                self.response.headers['Content-Type'] = 'text/html'
                self.response.write( bad_login )
        else:
            request_login = '''
                <div style="background-color:#3A373D;text-align:center;color:white;padding:2%;border:1px solid #356CA9;">
                    <img src="/resources/images/logo-clever.png" />
                    <h2>Please login with your @clever.com email to view this project</h2>
                    <a href="'''+users.create_login_url('/')+'''" style="color:white;">Login using Google API</a>
                </div>
            '''
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write( request_login )
    # ---------- ---------- ---------- ---------- ---------- #
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
application = webapp2.WSGIApplication([ # Map URL requests to classes
    ('/clever.*',           GetClever),
    ('/changelog.*',        GetChangelog),
    
    ('/resources/css.*',    GetCSS),
    ('/resources/js.*',     GetJS),
    
    ('/.*',                 GetPage) # MainPage that is the default for all URLs sans the ones listed above. All URLs go to MainPage: /index, /home, /changelog, etc.
], debug=True)
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

