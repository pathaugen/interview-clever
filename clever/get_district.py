

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_district.py
description:  Fetching a specific district via JSON from Clever API.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


from clever.get_json_dict import get_json_dict


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_district( district_id ):
    district = ''
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    json_dict = get_json_dict('/v1.1/districts/'+district_id)
    # Pull pure district data (using district ID) as JSON from Clever API
    #clever += str( get_json('/v1.1/districts/4fd43cc56d11340000000005') )
    '''
        {
            u'links':[
                {
                    u'uri':    u'/v1.1/districts/4fd43cc56d11340000000005',
                    u'rel':    u'self'
                },
                {
                    u'uri':    u'/v1.1/districts/4fd43cc56d11340000000005/schools',
                    u'rel':    u'schools'
                },
                {
                    u'uri':    u'/v1.1/districts/4fd43cc56d11340000000005/teachers',
                    u'rel':    u'teachers'
                },
                {
                    u'uri':    u'/v1.1/districts/4fd43cc56d11340000000005/students',
                    u'rel':    u'students'
                },
                {
                    u'uri':    u'/v1.1/districts/4fd43cc56d11340000000005/sections',
                    u'rel':    u'sections'
                },
                {
                    u'uri':    u'/v1.1/districts/4fd43cc56d11340000000005/events',
                    u'rel':    u'events'
                }
            ],
            u'data':{
                u'name':       u'Demo District',
                u'id':         u'4fd43cc56d11340000000005'
            }
        }
    '''
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    for link in json_dict['links']:
        district_add = '<div class="district-link"><h3>{NAME}</h3><div class="district-uri">URI: {URI}</div></div>'
        
        district_add = district_add.replace( '{NAME}', link['rel'] )
        district_add = district_add.replace( '{URI}', link['uri'] )
        
        district += district_add
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    return district
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

