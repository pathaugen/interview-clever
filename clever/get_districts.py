

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_districts.py
description:  Fetching the districts via JSON from Clever API.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


from clever.get_json_dict import get_json_dict


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_districts( ):
    districts = ''
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    json_dict = get_json_dict('/v1.1/districts')
    '''
        {
            u'paging':{
                u'total':         1,
                u'current':       1,
                u'count':         1
            },
            u'links':[
                {
                    u'rel':       u'self',
                    u'uri':       u'/v1.1/districts'
                }
            ],
            u'data':[
                {
                    u'data':{
                        u'id':    u'4fd43cc56d11340000000005',
                        u'name':  u'Demo District'
                    },
                    u'uri':       u'/v1.1/districts/4fd43cc56d11340000000005'
                }
            ]
        }
    '''
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    for district in json_dict['data']:
        district_add = open('clever/district.html').read() # Load district template HTML file
        
        district_add = district_add.replace( '{NAME}', district['data']['name'] )
        district_add = district_add.replace( '{ID}', district['data']['id'] )
        
        districts += district_add
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    return districts
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

