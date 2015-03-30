

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_school.py
description:  Fetching a specific school via JSON from Clever API.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


from clever.get_json_dict import get_json_dict


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_school( school_id ):
    school = ''
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    json_dict = get_json_dict('/v1.1/schools/'+school_id)
    # Pull school data (using school ID) as JSON from Clever API
    #clever += str( get_json('/v1.1/schools/530e595026403103360ff9fd') )
    '''
        {
            u'data':{
                u'phone':            u'(212) 555-1212',                  -> PHONE
                u'state_id':         u'712345',
                u'location':{
                    u'zip':          u'10001',                           -> ZIP
                    u'address':      u'350 5th Avenue',                  -> ADDRESS
                    u'state':        u'NY',                              -> STATE
                    u'city':         u'New York'                         -> CITY
                },
                u'high_grade':       u'12',                              -> HIGH_GRADE
                u'sis_id':           u'02M800',
                u'principal':{
                    u'email':        u'tdkhan@mailinator.com',           -> PRINCIPAL_EMAIL
                    u'name':         u'Theodora Khan'                    -> PRINCIPAL_NAME
                },
                u'school_number':    u'02M800',                          -> SCHOOL_NUMBER
                u'last_modified':    u'2014-02-26T21:14:56.665Z',
                u'district':         u'4fd43cc56d11340000000005',
                u'id':               u'530e595026403103360ff9fd',        -> ID: This is the ID used for URI and the links
                u'nces_id':          u'360008000000',
                u'created':          u'2014-02-26T21:14:56.662Z',
                u'name':             u'Clever High School',              -> NAME
                u'low_grade':        u'9'                                -> LOW_GRADE
            },
            u'links':[
                {
                    u'rel': u'self',
                    u'uri': u'/v1.1/schools/530e595026403103360ff9fd'
                },
                {
                    u'rel': u'district',
                    u'uri': u'/v1.1/schools/530e595026403103360ff9fd/district'
                },
                {
                    u'rel': u'teachers',
                    u'uri': u'/v1.1/schools/530e595026403103360ff9fd/teachers'
                },
                {
                    u'rel': u'students',
                    u'uri': u'/v1.1/schools/530e595026403103360ff9fd/students'
                },
                {
                    u'rel': u'sections',
                    u'uri': u'/v1.1/schools/530e595026403103360ff9fd/sections'
                },
                {
                    u'rel': u'events',
                    u'uri': u'/v1.1/schools/530e595026403103360ff9fd/events'
                }
            ]
        }
    '''
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    '''
    for link in json_dict['links']:
        school_add = '<div class="school-link"><h3>{NAME}</h3><div class="school-uri">URI: {URI}</div></div>'
        school_add = school_add.replace( '{NAME}', link['rel'] )
        school_add = school_add.replace( '{URI}', link['uri'] )
        school += school_add
    '''
    #for data in json_dict['data']:
    
    
    school_add = '''
        <div id="popup-picture">
            <img src="/resources/images/school-icon.png" />
        </div>
        
        
        <div id="popup-school">
            <h1>{NAME}</h1>
            <div class="popup-school-info">
                <h3>ID:</h3>
                {ID}
            </div>
            <div class="popup-school-info">
                <h3>School #:</h3>
                {SCHOOL_NUMBER}
            </div>
            <div class="popup-school-info">
                {ADDRESS}
                <br />{CITY}, {STATE} {ZIP}
            </div>
            <div class="popup-school-info">
                <h3>Grades:</h3>
                {LOW_GRADE} - {HIGH_GRADE}
            </div>
            <div class="popup-school-info">
                <h3>Phone:</h3>
                {PHONE}
            </div>
            <div class="popup-school-info">
                <h3>Principal:</h3>
                <a href="mailto:{PRINCIPAL_EMAIL}">{PRINCIPAL_NAME}</a>
            </div>
        </div>
        
        <script>
            /* ---------- ---------- ---------- ---------- ---------- */
            $(function() {
                var map = L.map('map-{ID}', {
                    scrollWheelZoom: false
                }).setView([{GEO}], 14);
                
                L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                    maxZoom: 18
                }).addTo(map);
                
                var marker = L.marker( [{GEO}] ).addTo(map);
                marker.bindPopup("<b>{NAME}</b><br />{ADDRESS}<br />{CITY}, {STATE} {ZIP}<br />Grades: {LOW_GRADE} - {HIGH_GRADE}<br />Phone: {PHONE}").openPopup();
            });
            /* ---------- ---------- ---------- ---------- ---------- */
        </script>
        <div class="map-container">
            <h1>Map and Driving Directions</h1>
            <div class="map" id="map-{ID}">
                <h2>Map</h2>
            </div>
        </div>
    '''
    
    
    # Geo coords for the schools
    if json_dict['data']['school_number'] == '02M800':      school_geo = '40.74838, -73.98548' # 350 5th Avenue, New York, NY 10001
    elif json_dict['data']['school_number'] == '13K123':    school_geo = '40.69808, -73.99273' # 110 Pineapple Street, Brooklyn, NY 11201
    elif json_dict['data']['school_number'] == '27Q321':    school_geo = '40.58919, -73.81320' # 322 Old Beach 88th Street, Rockaway Beach, NY 11693
    else:                                                   school_geo = '37.78732835, -122.399375199131' # Clever HQ
    
    school_add = school_add.replace( '{GEO}',               school_geo )
    
    
    school_add = school_add.replace( '{PHONE}',             json_dict['data']['phone'] )
    school_add = school_add.replace( '{ZIP}',               json_dict['data']['location']['zip'] )
    school_add = school_add.replace( '{ADDRESS}',           json_dict['data']['location']['address'] )
    school_add = school_add.replace( '{STATE}',             json_dict['data']['location']['state'] )
    school_add = school_add.replace( '{CITY}',              json_dict['data']['location']['city'] )
    school_add = school_add.replace( '{HIGH_GRADE}',        json_dict['data']['high_grade'] )
    school_add = school_add.replace( '{PRINCIPAL_EMAIL}',   json_dict['data']['principal']['email'] )
    school_add = school_add.replace( '{PRINCIPAL_NAME}',    json_dict['data']['principal']['name'] )
    school_add = school_add.replace( '{SCHOOL_NUMBER}',     json_dict['data']['school_number'] )
    school_add = school_add.replace( '{ID}',                json_dict['data']['id'] )
    school_add = school_add.replace( '{NAME}',              json_dict['data']['name'] )
    school_add = school_add.replace( '{LOW_GRADE}',         json_dict['data']['low_grade'] )
    
    
    school += school_add
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    return school
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

