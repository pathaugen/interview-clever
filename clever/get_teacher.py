

''' ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
file-name:    get_teacher.py
description:  Fetching a specific teacher via JSON from Clever API.
last-update:  2015-03-29: Sunday
updated-by:   Patrick Haugen (pathaugen@gmail.com)
---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- '''


from clever.get_json_dict import get_json_dict


# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
def get_teacher( teacher_id ):
    teacher = ''
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    json_dict = get_json_dict('/v1.1/teachers/'+teacher_id)
    # Pull teacher data (using teacher ID) as JSON from Clever API
    '''
        {
            u'links':[
                {
                    u'uri': u'/v1.1/teachers/50c20477987eda0d3d02d310',
                    u'rel': u'self'
                },
                {
                    u'uri': u'/v1.1/teachers/50c20477987eda0d3d02d310/district',
                    u'rel': u'district'
                },
                {
                    u'uri': u'/v1.1/teachers/50c20477987eda0d3d02d310/school',
                    u'rel': u'school'
                },
                {
                    u'uri': u'/v1.1/teachers/50c20477987eda0d3d02d310/students',
                    u'rel': u'students'
                },
                {
                    u'uri': u'/v1.1/teachers/50c20477987eda0d3d02d310/sections',
                    u'rel': u'sections'
                },
                {
                    u'uri': u'/v1.1/teachers/50c20477987eda0d3d02d310/grade_levels',
                    u'rel': u'grade_levels'
                },
                {
                    u'uri': u'/v1.1/teachers/50c20477987eda0d3d02d310/events',
                    u'rel': u'events'
                }
            ],
            u'data':{
                u'credentials':{
                    u'district_username': u'jessica.stark',
                    u'district_password': u'EGhaingi4qu'
                },
                u'district': u'4fd43cc56d11340000000005',
                u'name':{
                    u'last': u'Stark',
                    u'first': u'Jessica',
                    u'middle': u'R'
                },
                u'school': u'530e595026403103360ff9fe',
                u'created': u'2012-12-07T15:00:07.733Z',
                u'sis_id': u'70',
                u'id': u'50c20477987eda0d3d02d310',
                u'last_modified': u'2014-02-26T21:15:01.451Z',
                u'teacher_number': u'459202',
                u'email': u'stark_jessica@example.net',
                u'title': u'Kindergarten Teacher'
            }
        }
    '''
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    # ---------- ---------- ---------- ---------- ---------- #
    #teacher += str(json_dict)
    
    
    teacher += '''
        <div id="popup-picture">
            <img src="/resources/images/user-icon.png" />
        </div>
        <div id="popup-teacher">
            <h1>{LASTNAME}, {FIRSTNAME} {MIDDLENAME}</h1>
            <div class="popup-teacher-info">
                <h3>{TITLE}</h3>
            </div>
            <div class="popup-teacher-info">
                <h3>ID:</h3>
                {ID}
            </div>
            <div class="popup-teacher-info">
                <h3>Teacher #:</h3>
                {TEACHERNUMBER}
            </div>
            <div class="popup-teacher-info">
                <h3>Email:</h3>
                <a href="mailto:{EMAIL}">{EMAIL}</a>
            </div>
            <div class="popup-teacher-info">
                <h3>Username:</h3>
                {USERNAME}
            </div>
            <div class="popup-teacher-info">
                <h3>Password:</h3>
                {PASSWORD}
            </div>
        </div>
    '''
    
    
    teacher = teacher.replace( '{LASTNAME}',        json_dict['data']['name']['last'] )
    teacher = teacher.replace( '{FIRSTNAME}',       json_dict['data']['name']['first'] )
    teacher = teacher.replace( '{MIDDLENAME}',      json_dict['data']['name']['middle'] )
    teacher = teacher.replace( '{TITLE}',           json_dict['data']['title'] )
    teacher = teacher.replace( '{ID}',              json_dict['data']['id'] )
    teacher = teacher.replace( '{TEACHERNUMBER}',   json_dict['data']['teacher_number'] )
    teacher = teacher.replace( '{EMAIL}',           json_dict['data']['email'] )
    teacher = teacher.replace( '{USERNAME}',        json_dict['data']['credentials']['district_username'] )
    teacher = teacher.replace( '{PASSWORD}',        json_dict['data']['credentials']['district_password'] )
    # ---------- ---------- ---------- ---------- ---------- #
    
    
    return teacher
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

